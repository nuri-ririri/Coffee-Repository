import random
# bot has username: @mokaCoffee_bot
import telebot
from telebot import types

bot = telebot.TeleBot('6229541150:AAERERI4b2QVw4CmP8tmTXQEfb96ovJu5KE')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    bot.send_message(message.from_user.id,
                     f"<b>Gutto Morning, {message.from_user.first_name}, Get whatever coffee you want! \n</b>",
                     parse_mode='html')
    bot.send_message(message.chat.id, "Today is a "
                                      f"good day for a cup of tough coffee, don't you think so??\n right 'meme', please:)",
                     parse_mode='html')
    menu = types.KeyboardButton('menu')
    events = types.KeyboardButton('Special Events')
    human = types.KeyboardButton('Chat with Manager')
    order = types.KeyboardButton('Make on order')
    markup.add(menu, order, events, human)
    bot.send_dice(message.chat.id, "🎰", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text in {'Hello', 'hello', 'Hi', 'hi', 'Ohayo gosaimasu, senpai'}:
        bot.send_message(message.chat.id, "Hello to you too:) How can I help you?", parse_mode='html')
    elif message.text in {'meme', 'gimme meme', '/meme'}:
        bot.send_message(message.chat.id, "wait a minute, meme is loading...")
        picture = random.randint(0, 11)
        meme = open(f"memes/{picture}.jpeg", 'rb')
        bot.send_photo(message.chat.id, meme)
    elif message.text == 'menu':
        bot.send_photo(message.chat.id, open("menu.jpeg", "rb"))
    elif message.text == "Special Events":
        bot.send_message(message.chat.id, "No special events scheduled, sumimasen")
    elif message.text == "Chat with Manager":
        manager = types.InlineKeyboardMarkup()
        manager.add(types.InlineKeyboardButton("Manager", url="https://web.telegram.org/k/#@fwtbh"))
        bot.send_message(message.chat.id, "Chat with", reply_markup=manager)
    else:
        bot.send_message(message.chat.id, "Lost connection with your idea", parse_mode='html')


bot.polling(none_stop=True)
