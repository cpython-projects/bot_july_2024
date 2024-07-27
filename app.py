import telebot
from dotenv import load_dotenv
import os
from flask import Flask, request

load_dotenv()

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


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


@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return 'Test Bot', 200


@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://july-bot-606ff6a196f8.herokuapp.com/' + TOKEN)
    return 'Test Bot', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))





























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
