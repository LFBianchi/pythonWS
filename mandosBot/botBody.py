import scrapper
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler

greetings = "I'm mandosBot, just say the word and I will send my eagles to fetch the prices of LATAM multiplus tickets!"

updater = Updater(token='1461875156:AAGjqlo73W2xKZ4FXwveulS7W5wVQ8WpPEk',
                  use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=greetings)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
