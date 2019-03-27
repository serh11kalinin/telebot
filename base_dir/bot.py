# -*- coding: utf-8 -*-
from base_dir import config
import telebot
import os
import time

bot = telebot.TeleBot(config.token)

"""
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
"""


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            # sending file_id after file itself
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)


if __name__ == '__main__':
    bot.polling(none_stop=True)

