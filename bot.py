import asyncio 
import random
from aiogram import Bot, Dispatcher, types 
from aiogram.types import(ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton)
from aiogram.filters import Command 
from aiogram.client.default import DefaultBotProperties
from weather import get_weather
from api import TOKEN

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher() 
 
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Привет!"), KeyboardButton(text="Помощь")]
    ],
    resize_keyboard=True
)


inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Начать", callback_data="start")],
        [InlineKeyboardButton(text="Помощь", callback_data="help")],
        [InlineKeyboardButton(text="Рандомное число", callback_data="random")]
    ]
)

@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data =="start" :
      await callback.message.answer("Напиши  /start , что бы начать работу с ботом")
    elif callback.data =="help" :
         await callback.message.answer("Альтернативная помощь или напиши /help")
    elif callback.data =="random" :
        await callback.message.answer("Хочешь рандомное число? напиши: /random")
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я тестовый бот <b>test</b>", reply_markup=main_keyboard)

@dp.message(Command("random"))
async def random_commamnd(message: types.Message):
      number = random.randint(1,100)
      await message.answer(f"Случайное число: {number}")

@dp.message(Command("help"))
async def help_command(message: types.message):
    command_text=(
        "Доступные комманды:\n"
        "/start- Начать  работу с ботом\n"
        "/help - Показывает список команд\n"
        "/random - Случайное число\n"
    )
    await message.answer(command_text)
@dp.message(Command("weather"))
async def weather_command(message: types.message):
    weather_info = await get_weather()
    await message.reply (weather_info)

@dp.message(lambda message: message.text == "Привет!")
async def hello(message: types.Message):
    await message.answer("Привет!!! Как дела?", reply_markup=inline_keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())