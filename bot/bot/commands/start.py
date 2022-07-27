from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command


# @router_start.message(commands=['start'])
# async def start(message: types.message):
#     start_button = ['weather', 'poetry', 'chatterbox']
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(*start_button)
#
#     await message.answer('Привет, что ты хочешь?', reply_markup=keyboard)
