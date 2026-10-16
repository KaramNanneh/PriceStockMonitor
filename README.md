# Telegram Price & Stock Monitor

A background Python application that monitors web pages for prices, restocks, and matching listings, sending automated instant Telegram notifications directly to your phone.

## Overview

This project automates tracking product availability and price drops. 

Built with Python, the application fetches target URLs using custom headers to bypass blocks, parses product data and stock status using BeautifulSoup, evaluates conditions against user-defined thresholds, and triggers real-time alerts via the Telegram Bot API.

## Features

* **Automated Web Tracking:** Continuously checks products price and stock in 5 minute interval.
* **Price Tracking:** Checks product price against target price.
* **Stock Monitoring:** Checks product availability.
* **Telegram Notifications:** Sends mobile notifications.
* **Error Logs:** Provides simple console feedback on errors encountered.

## Application Preview

### 1. Terminal Execution & Debug Log
![Terminal Execution](docs/screenshots/terminal-log.png)

### 2. Telegram Phone Notification
![Telegram Alert](docs/screenshots/telegram-alert.png)

## Getting Started
* **Python installed on your computer.**
* **A Telegram account to configure your bot and retrieve your chat ID.**
* **The project dependencies listed in requirements.txt.**

### Installation
Clone the repository:
git clone [https://github.com/KaramNanneh/telegram-price-monitor.git](https://github.com/KaramNanneh/telegram-price-monitor.git)
cd telegram-price-monitor

Install the Python dependencies:
pip install -r requirements.txt

Open monitor.py and input your credentials and target item:
Insert your Telegram Bot Token.
Insert your Telegram Chat ID.
Set your TARGET_URL and desired TARGET_PRICE.
ENJOY!
