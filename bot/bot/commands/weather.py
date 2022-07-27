from aiogram import types
import requests
import datetime
from bot.bot.config import token_weather
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters import Command



#@router_weather.message(Text(text='weather'))
# @router_weather.message(commands='weather')
# async def q_weather(message: types.message):
#     await message.answer('В каком городе посмотреть погоду?')
#
#     @router_weather.message()
#     async def get_weather(message: types.message):
#         try:
#             r = requests.get(
#                 f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token_weather}&units=metric")
#             data = r.json()
#             city = data["name"]
#             temp = data["main"]["temp"]
#             await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
#                                 f"Температура в городе {city} составляет: {temp}C°"
#                                 )
#         except:
#             await message.answer('Я такого города не знаю. Извини')

