import requests
from bs4 import BeautifulSoup
import time
import telegram

# Setup Telegram Bot
bot = telegram.Bot(token='')
chat_id = '1123870739'

# Set up web scraper
url = 'https://www.iplt20.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the relevant information on the webpage
ticket_availability = soup.find('div', {'class': 'ticket__availability'}).text

# Check for ticket availability changes
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    new_ticket_availability = soup.find('div', {'class': 'ticket__availability'}).text

    if new_ticket_availability != ticket_availability:
        ticket_availability = new_ticket_availability
        message = "IPL ticket availability has changed. The new status is: " + ticket_availability
        bot.send_message(chat_id=chat_id, text=message)
    time.sleep(60) # Wait for 60 seconds before checking again
