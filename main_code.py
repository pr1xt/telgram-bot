import random
from aiogram import Bot, Dispatcher, types, executor
from config import TOKEN_API


DESCRIPTION = "I'm bot on python"
LETTERS = "qwertyuiopasdfghjklzxcvbnm"
HELP_COMMAND = """
/help - list
/start - start
/random - random letter
/description - who is it?
/count - gives a count of calls to bot
"""

count_of_calls = 0
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


@dp.message_handler(commands=["help"])
async def help(message: types.Message):
    await message.reply(text=HELP_COMMAND)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(text="Hello")
    await message.delete()

@dp.message_handler(commands=["random"])
async def random_letter(message: types.Message):
    await message.answer(text=random.choice(LETTERS))

@dp.message_handler(commands=["description"])
async def description(message: types.Message):
    await message.answer(text=DESCRIPTION)

@dp.message_handler(commands=["count"])
async def calls_count(message: types.Message):
    global count_of_calls
    await message.answer(f"calls: {count_of_calls}")
    count_of_calls += 1

@dp.message_handler()
async def echo(message: types.Message):
    if message.text.find("0") > 0:
        await message.reply("Y")
    else:
        await message.reply("N")


if __name__ == '__main__':
    executor.start_polling(dp)