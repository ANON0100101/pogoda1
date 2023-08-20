
import telebot
import requests
import json
# from telebot import types

bot = telebot.TeleBot('6238923621:AAHkpONuQADuiqu1BuL31ii5jVVHFvGMjkY')
API = '73e43eccf3edd686f2abed104ac7aaae'



@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi, good to see u! send name of the city')


@bot.message_handler(content_types = ['text'])
def get_weather(message):
    city = message.text.strip().title()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'In {city} {temp}°C right now')
        # image = '26.png' if temp > 10 else '27.png'
        # file_ = open('./' + image, 'rb')
        # bot.send_photo(message.chat.id, file_)
    else:
        bot.reply_to(message, 'city is incorrect')


bot.polling(none_stop = True)

