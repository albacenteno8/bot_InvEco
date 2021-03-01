# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 20:48:51 2021

@author: alba_
"""


import pandas as pd
import os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import logging


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', '8443'))

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    
def process_names():
    list_of_re = pd.read_csv("list_has.csv")
    list_names = list_of_re['Name'].tolist()
    list_names1 = list()

    for i in list_names:
        name = [i.strip("#") for i in i.split() if i.startswith("#")]
        name = name[0]
        list_names1.append('#'+name)
        
    return list_names1
    
def process_message(update, context):
    
    list_names_has = process_names()
    text = update.message.text
    
    try:
        hast_group = [text.strip("#") for text in text.split() if text.startswith("#")]
        hast_group = '#'+hast_group[0]
    except:
        hast_group = '#NONONONONO'
        
    if hast_group in list_names_has: 
        context.bot.send_message(chat_id='-1001424788869',text=text)

def main():
    """Start the bot."""
    
    TOKEN = '1697060227:AAHy2-dNaVy5dRA1oF-8g6GwyA62xEXFQW8'
    APP_NAME = 'reenvioeco12'
    #PORT = int(os.environ.get('PORT', 5000))
    
    updater = Updater(token=TOKEN, use_context=True)

    dp = updater.dispatcher
    
    dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    #dp.add_error_handler(error)
    #updater.start_polling()
    
        # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook(APP_NAME + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    print('Bot is polling')
    updater.idle()

if __name__ == '__main__':
    main()