# Telegram Price & Stock Monitor

A background Python application that monitors web pages for prices, restocks, and matching listings, sending automated instant Telegram notifications directly to your phone.

## Overview

This project automates tracking product availability and price drops. 

Built with Python, the application fetches target URLs using custom headers to bypass blocks, parses product data and stock status using BeautifulSoup, evaluates conditions against user-defined thresholds, and triggers real-time alerts via the Telegram Bot API.

## Features

* **Automated Web Tracking:** Continuously monitors product pages at configurable time intervals.
* **Price Tracking:** Extracts and evaluates current product pricing against a target budget.
* **Stock Monitoring:** Inspects page availability elements to detect restocks or out-of-stock changes.
* **Instant Telegram Alerts:** Sends direct mobile notifications via the Telegram Bot API when target criteria are met.
* **Robust Request Headers:** Utilizes custom User-Agents and languages to ensure stable scraping connectivity.
* **Error & Debug Logging:** Provides clean console feedback tracking HTTP status codes, parsed prices, and API delivery responses.

## Application Preview

### 1. Terminal Execution & Debug Log
![Terminal Execution](docs/screenshots/terminal-log.png)

### 2. Telegram Phone Notification
![Telegram Alert](docs/screenshots/telegram-alert.png)

## How It Works

1. **Target Setup:** The script is configured with a target product URL, budget price limit, and check frequency.
2. **Request Execution:** Background loops send HTTP GET requests with custom browser headers to the target site.
3. **HTML Parsing:** BeautifulSoup extracts the specific price tag and stock availability status container from the HTML.
4. **Data Cleaning:** Price text is scrubbed of currency symbols and commas, then converted into a float value.
5. **Condition Evaluation:** The app verifies if the product is in stock and if the current price matches or falls below your target.
6. **Notification Trigger:** If conditions match, an automated message payload is dispatched instantly to your Telegram chat.
7. **Interval Sleep:** The script pauses for the defined check interval before repeating the background cycle.

---

## Project Structure

```text
PriceMonitor/
├── monitor.py
├── requirements.txt
├── README.md
└── docs/
    └── screenshots/
        ├── terminal-log.png
        └── telegram-alert.png# Telegram Price & Stock Monitor

A background Python application that monitors web pages for prices, restocks, and matching listings, sending automated instant Telegram notifications directly to your phone.

## Overview

This project automates tracking product availability and price drops. 

Built with Python, the application fetches target URLs using custom headers to bypass blocks, parses product data and stock status using BeautifulSoup, evaluates conditions against user-defined thresholds, and triggers real-time alerts via the Telegram Bot API.

## Features

* **Automated Web Tracking:** Continuously monitors product pages at configurable time intervals.
* **Price Tracking:** Extracts and evaluates current product pricing against a target budget.
* **Stock Monitoring:** Inspects page availability elements to detect restocks or out-of-stock changes.
* **Instant Telegram Alerts:** Sends direct mobile notifications via the Telegram Bot API when target criteria are met.
* **Robust Request Headers:** Utilizes custom User-Agents and languages to ensure stable scraping connectivity.
* **Error & Debug Logging:** Provides clean console feedback tracking HTTP status codes, parsed prices, and API delivery responses.

## Application Preview

### 1. Terminal Execution & Debug Log
![Terminal Execution](docs/screenshots/terminal-log.png)

### 2. Telegram Phone Notification
![Telegram Alert](docs/screenshots/telegram-alert.png)

## How It Works

1. **Target Setup:** The script is configured with a target product URL, budget price limit, and check frequency.
2. **Request Execution:** Background loops send HTTP GET requests with custom browser headers to the target site.
3. **HTML Parsing:** BeautifulSoup extracts the specific price tag and stock availability status container from the HTML.
4. **Data Cleaning:** Price text is scrubbed of currency symbols and commas, then converted into a float value.
5. **Condition Evaluation:** The app verifies if the product is in stock and if the current price matches or falls below your target.
6. **Notification Trigger:** If conditions match, an automated message payload is dispatched instantly to your Telegram chat.
7. **Interval Sleep:** The script pauses for the defined check interval before repeating the background cycle.

---

## Project Structure

```text
PriceMonitor/
├── monitor.py
├── requirements.txt
├── README.md
└── docs/
    └── screenshots/
        ├── terminal-log.png
        └── telegram-alert.png
