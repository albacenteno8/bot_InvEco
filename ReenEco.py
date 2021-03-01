# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 17:43:26 2021

@author: alba_
"""

import pandas as pd
import os
from telegram.ext import Updater, MessageHandler, Filters


PORT = int(os.environ.get('PORT', 5000))

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

if __name__ == '__main__':
    updater = Updater(token='1697060227:AAHy2-dNaVy5dRA1oF-8g6GwyA62xEXFQW8', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))
    updater.start_polling()

    print('Bot is polling')

    updater.idle()
