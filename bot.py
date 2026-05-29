import os
import requests
from bs4 import BeautifulSoup
import telebot

token = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(token)

def get_from_cite(query):
    url = 'http://l993046g.beget.tech/index.php'
    headers = {"User-Agent": "Mozilla/5.0"}
    payload = {'query': query}

    doc = requests.get(url, headers=headers, params=payload)

    if doc.status_code == 200:
        soup = BeautifulSoup(doc.text, 'html.parser')
        return soup.body.get_text(separator='\n', strip=True)
    else:
        return f"Ошибка {doc.status_code}"

@bot.message_handler(content_types=['text'])
def handle(message):
    result = get_from_cite(message.text)
    bot.send_message(message.chat.id, result)

bot.infinity_polling()