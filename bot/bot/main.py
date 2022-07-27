from aiogram import Dispatcher, Bot, types
import logging
import requests
import datetime
from commands.chatterbox import respond_to_dialog
from aiogram.dispatcher.filters import Text
from config import token_weather
from config import token_bot
import asyncio
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained('/home/anton/Desktop/tg_bot/bot/models/tokenizer_tg')
model = AutoModelForCausalLM.from_pretrained("/home/anton/Desktop/tg_bot/bot/models/model_for_tg")
bot = Bot(token=token_bot)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.message):
    start_button = ['weather', 'poetry', 'chatterbox']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_button)

    await message.answer('Привет, что ты хочешь?', reply_markup=keyboard)

@dp.message_handler(Text(equals='weather'))
@dp.message_handler(commands='weather')
async def q_weather(message: types.message):
    await message.answer('В каком городе посмотреть погоду?')

    @dp.message_handler()
    async def get_weather(message: types.message):
        try:
            r = requests.get(
                f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token_weather}&units=metric")
            data = r.json()
            city = data["name"]
            temp = data["main"]["temp"]
            await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
                                f"Температура в городе {city} составляет: {temp}C°"
                                )
        except:
            await message.answer('Я такого города не знаю. Извини')

@dp.message_handler(Text(equals='chatterbox'))
@dp.message_handler(commands='chatterbox')
async def q_chatterbox(message: types.message):
    await message.answer('О чем поговорим?')

    @dp.message_handler()
    async def chatterbox(message: types.message):
        seed = message.text
        history = [seed]
        result = respond_to_dialog(history[-10:])
        next_sentence = result

        await message.answer(f'{next_sentence}')

@dp.message_handler(Text(equals='poetry'))
@dp.message_handler(commands='poetry')
async def q_poetry(message: types.Message):
    await message.answer('Начни, а я продолжу..')

    @dp.message_handler()
    async def poetry(message: types.Message):
        prefix = message.text
        tokens = tokenizer(prefix, return_tensors='pt')
        size = tokens['input_ids'].shape[1]
        output = model.generate(
            **tokens,
            do_sample=False,

            max_length=size+500,
            repetition_penalty=5.,
            temperature=0.8,
            num_beams=10,
        )
        decoded = tokenizer.decode(output[0])
        result = decoded[len(prefix):]
        await message.reply(prefix + result)

async def main():
    logging.basicConfig(level=logging.DEBUG)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
