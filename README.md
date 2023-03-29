# Krayot314zdoduy-Mon
Weather Notifier

This Python script retrieves the current weather conditions from a website and sends notifications through Telegram during working hours (5 AM to 8 PM). The script fetches weather information such as wind direction, wind speed, maximum wind speed, and temperature, and sends the data as a formatted message to a specified Telegram chat.
Prerequisites

Before using this script, you need to have Python 3.7 or higher installed on your system. Additionally, you will need the following Python packages:

    beautifulsoup4
    requests
    telegram
    pytz

You can install these packages using pip:


pip install beautifulsoup4 requests python-telegram-bot pytz

Setup

    Create a new bot on Telegram by talking to the BotFather.
    After creating the bot, you will receive a bot token. Replace YOUR_TOKEN in the script with your bot token.
    Add the bot to a Telegram group or chat, and then use the IDBot to get the chat ID of the group or chat. Replace YOUR_CHAT_ID in the script with your chat ID.

Usage

To run the script, simply execute it with Python:


python weather_notifier.py

The script will fetch the weather information every 5 minutes and send notifications to the specified Telegram chat during working hours (5 AM to 8 PM).
