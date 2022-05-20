from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

bot = Bot(token='5319001869:AAExMCObJ9emuHyIwwL0zGGEaBU8Kpx6YfM', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_button = 'Show knives'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(start_button)

    await message.answer('Tap the key', reply_markup=keyboard)


@dp.message_handler(Text(equals='Show knives'))
async def get_knives(message: types.Message):
    await message.answer('Please wait ...')


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()