import telebot
import config
from telebot import types
import random

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/aaaaa.png', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Добро пожаловать.\n Я - тестовый бот".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])

def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Рандомное число":
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "Как дела?":

            markup = types.InlineKeyboardMarkup(row_width = 2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='Good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='Bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, "Отлично, ты как?", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Я не знаю, что ответить.\n Еще не научился :(")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == "Good":
                bot.send_message(call.message.chat.id, "Вот и отлично")
            elif call.data == "Bad":
                bot.send_message(call.message.chat.id, "Бывает, но все будет хорошо")

            bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.message_id, text="Как дела?", reply_markup=None)

    except Exception as e:
        print(repr(e))            

bot.polling(non_stop=True)