from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
from main import collect_data
import time

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

    collect_data()
    with open('result.json', encoding='utf-8') as file:
        data = file.read()

    for index, item in enumerate(collect_data()):
        card = f'{hlink(item.get("item_name"), item.get("item_url"))}\n' \
            f'{hbold("Price: ")}{item.get("item_price")}%\n' \

        if index%8 == 0:
            time.sleep(3)

        await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()