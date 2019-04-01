# -*- coding: utf-8 -*-
import telebot
from base_dir import config
import os
import time
import random
from base_dir import utils
from base_dir.SQLighter import SQLighter
from telebot import types

bot = telebot.TeleBot(config.token)

"""
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)



if __name__ == '__main__':
    bot.polling(none_stop=True)
"""


@bot.message_handler(commands=['game'])
def game(message):
    # Подключаемся к БД
    db_worker = SQLighter(config.database_name)
    # Получаем случайную строку из БД
    row = db_worker.select_single(random.randint(1, utils.get_rows_count()))
    # Формируем разметку
    markup = utils.generate_markup(row[2], row[3])
    # Отправляем аудиофайл с вариантами ответа
    bot.send_voice(message.chat.id, row[1], reply_markup=markup, duration=20)
    # Включаем "игровой режим"
    utils.set_user_game(message.chat.id, row[2])
    # Отсоединяемся от БД
    db_worker.close()


@bot.message_handler(func=lambda message: True, content_types=['text'])
def check_answer(message):
    # if func returns None - user is out of the game
    answer = utils.get_answer_for_user(message.chat.id)
    # answer could be a text as well as None
    # if answer is None
    if not answer:
        bot.send_message(message.chat.id, 'Choose /game command to start the game')
    else:
        # closing keyboard with possible answers
        keyboard_hider = types.ReplyKeyboardRemove()
        # if answer right/wrong
        if message.text == answer:
            bot.send_message(message.chat.id, 'Right!', reply_markup=keyboard_hider)
        else:
            bot.send_message(message.chat.id, 'Sorry, that is wrong answer :( Try again!', reply_markup=keyboard_hider)
        # removing user from shelve (game over)
        utils.finish_user_game(message.chat.id)


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            msg = bot.send_voice(message.chat.id, f, None)
            print(msg)
            # sending file_id after file itself
            bot.send_message(message.chat.id, msg.voice.file_id, reply_to_message_id=msg.message_id)
        time.sleep(3)


if __name__ == '__main__':
    utils.count_rows()
    random.seed()
    bot.polling(none_stop=True)

