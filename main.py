import telebot
from telebot import types

bot = telebot.TeleBot('5552391840:AAG2b-8txRBooS8pj8XAIqQ2szwq51tE5c0')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'<b>Hello</b>, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "<b>And you Hello!</b>", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"<b>Your ID is: {message.from_user.id}</b>", parse_mode='html')
    elif message.text == "photo":
        photo = open('3064024.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    elif message.text == "Bye":
        bot.send_message(message.chat.id, f"<b>And you too Bye!</b>", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "<b>I don't understand you!</b>", parse_mode='html')


# @bot.message_handler(content_types=['photo'])
# def get_user_photo(message):
#     bot.send_message(message.chat.id, '<b>Wow, cool photo!</b>', parse_mode='html')
#
#
# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types. InlineKeyboardButton("Click to go to website", url="https://youtube.com"))
#     bot.send_message(message.chat.id, '<b>Sir,are you sure you want to go to the website?</b>', parse_mode='html', reply_markup=markup)
#
#
# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
#     website = types.KeyboardButton('/website')
#     start = types.KeyboardButton('/start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, 'Sir,are you sure you want to go to the website?', reply_markup=markup)


bot.polling(none_stop=True)
