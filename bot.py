import telebot
from telebot import types
from googletrans import Translator

bot = telebot.TeleBot("7102945008:AAFXqUcNjnLjKB4UV8IDNkz5g4TZU4UgK5M")

translator = Translator()

first_button = types.InlineKeyboardButton("channel", url="https://t.me/englishier")
second_button = types.InlineKeyboardButton("support", url="https://t.me/+UyUlyvDuoiUyYzU0")
markup = types.InlineKeyboardMarkup(row_width=1)
markup.add(first_button, second_button)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(f"Received start command from {message.chat.id}")
    bot.send_message(message.chat.id, "Hi guys!, I will translate message in this chat so that all people can understand each other.", reply_markup=markup)

key_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
key_markup.add("English", "Persian")

@bot.message_handler(commands=['help'])
def help_me(message):
    print(f"Received help command from {message.chat.id}")
    bot.reply_to(message, '''This is a smart translate that you can enter your text to translate it and make it available to you. By pressing the English key, it will convert the text from English to Farsi. And if Persian is pressed, it will translate the text from Persian to English‏''')

@bot.message_handler(func=lambda message: True)
def translate_message(message):
    print(message)
    if message.text.lower() == "english":
        print(f"Received English translation request from {message.chat.id}")
        bot.send_message(message.chat.id, "Please send the text you want to translate from English to Persian.")
        bot.register_next_step_handler(message, translate_to_persian)
    elif message.text.lower() == "persian":
        print(f"Received Persian translation request from {message.chat.id}")
        bot.send_message(message.chat.id, "لطفا متنی را که می خواهید از فارسی به انگلیسی ترجمه کنید ارسال کنید.")
        bot.register_next_step_handler(message, translate_to_english)
    else:
        print(f"Received message from {message.chat.id}: {message.text}")
        bot.send_message(message.chat.id, "Please select a language first.", reply_markup=key_markup)

def translate_to_persian(message):
    translated = translator.translate(message.text, dest='fa')
    bot.send_message(message.chat.id, translated.text)

def translate_to_english(message):
    translated = translator.translate(message.text, dest='en')
    bot.send_message(message.chat.id, translated.text)

print("Starting ...")
bot.polling(timeout=1000)