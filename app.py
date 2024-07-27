import telebot
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(commands=['help'])
def send_help(message):
    prompt = """
        /start - Start the bot
        /help - Get help
    """
    bot.reply_to(message, "Howdy, how are you doing?")


if __name__ == '__main__':
    bot.polling()






























# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
