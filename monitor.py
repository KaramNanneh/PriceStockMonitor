import time
import requests
from bs4 import BeautifulSoup

TELEGRAM_BOT_TOKEN = "8905422964:AAEec_N1E2o5nU9CcQs6c43uHRUrJ7a-4yk"
TELEGRAM_CHAT_ID = "7034434583"
CHECK_INTERVAL = 300

TARGET_URL = "https://www.amazon.co.uk/Amazon-T28B69-Luna-Wireless-Controller/dp/B0D8LJWZPB/ref=sr_1_1_ffob_sspa?crid=F8O4HAWGJJ09&dib=eyJ2IjoiMSJ9.vTmV39l1vL22P5Sx7oZJyWOOCDqtM7wHUOW4ZBTWyo6cxkhoxjZH1tJCcmy8-lCm1w6WxsgHERj7sjIlvtZlpDh7S8FIxRWmugxxu6tJyjEbQ8nRbigMii_cN3hl_k96BfVysUxrhvAwVNkuPfAY4eTywh3g1uZGYURyBc0c8NvN6tvDvTu2_jwlpx5GxYs2mwK04mdt3iIesUG1Czz7OCeAF267cmdlg-YQn-peGLc.nXUTDmEHTRFv4pu5MHlaGLURHCMeGI4ay0JCTXLPU78&dib_tag=se&keywords=controller&qid=1792173520&sprefix=controlle%2Caps%2C202&sr=8-1-spons&aref=8wh7JpLTt3&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
TARGET_PRICE = 59.99


def send_telegram_message(message):
  url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
  payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
  response = requests.post(url, json=payload, timeout=10)
  print("Telegram API Response:", response.json())


def check_product():
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
          " (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
      ),
      "Accept-Language": "en-US,en;q=0.9",
      "Accept": (
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
      ),
      "Referer": "https://www.google.com/",
  }
  try:
    response = requests.get(TARGET_URL, headers=headers, timeout=15)
    print(f"HTTP Status Code: {response.status_code}")
    if response.status_code != 200:
      print("Failed to load page.")
      return

    soup = BeautifulSoup(response.text, "html.parser")

    price_element = soup.select_one("span.a-price span.a-offscreen")
    availability_element = soup.select_one("#availability")

    if not price_element:
      print(
          "Could not find price element (Amazon may be blocking the request)."
      )
      return

    price_text = (
        price_element.text.strip()
        .replace("£", "")
        .replace("$", "")
        .replace(",", "")
    )
    current_price = float(price_text)
    print(f"Found Price: {current_price}")

    in_stock = True
    if availability_element and "out of stock" in availability_element.text.lower():
      in_stock = False

    if in_stock and current_price <= TARGET_PRICE:
      message = (
          f"Alert! Product is in stock and price is £{current_price}!"
          f" Check here: {TARGET_URL}"
      )
      send_telegram_message(message)
    else:
      print("Product is either out of stock or price is above target.")

  except Exception as e:
    print(f"An error occurred: {e}")


def main():
  while True:
    check_product()
    time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
  main()