import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup


logging.basicConfig(level=logging.INFO)


bot = Bot(token='6034341470:AAG6EOlhe78RN9--kk7Cv-ex8jrQXjhbeZk')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



class QuizState(StatesGroup):
    QUESTION_1 = State()
    QUESTION_2 = State()



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я бот-викторина. Ну что погнали?")



@dp.message_handler(Command('mem'))
async def send_mem(message: types.Message):

    await message.reply_photo(photo='https://avatars.dzeninfra.ru/get-zen_doc/5318099/pub_6239ec7f922ece7dd4ef90e8_6239ed470f586937d825b680/scale_1200')



import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup


logging.basicConfig(level=logging.INFO)


bot = Bot(token='6034341470:AAG6EOlhe78RN9--kk7Cv-ex8jrQXjhbeZk')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)



class QuizState(StatesGroup):
    QUESTION_1 = State()
    QUESTION_2 = State()



@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет! Я бот-викторина. Ну что погнали?")



@dp.message_handler(Command('mem'))
async def send_mem(message: types.Message):

    await message.reply_photo(photo='https://avatars.dzeninfra.ru/get-zen_doc/5318099/pub_6239ec7f922ece7dd4ef90e8_6239ed470f586937d825b680/scale_1200')



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "Кто создал Chatgpt?"
    answers = [
        "SpongeBob",
        "Elon Musk",
        "Sam Altman",
        "James Cameron",
        "Griffin",
        "Hideo Kodzima",
    ]

    # await bot.send_poll()
    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Не грусти, все мы ошибаемся!",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    quiestion = "В каком году был основан Geeks?"
    answers = [
        "2008",
        "2015",
        "2018",
        "2020",
        "Я не знаю",
    ]

    # await bot.send_poll()
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Попробуй еще раз, я верю в тебя!",
        open_period=10,
    )



@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_message_or_square_number(message: types.Message):
    if message.text.isdigit():
        square = int(message.text) ** 2
        await message.answer(f"Квадрат числа: {square}")
    else:
        await message.answer(message.text)


if __name__ == '__main__':

    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)



@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_message_or_square_number(message: types.Message):
    if message.text.isdigit():
        square = int(message.text) ** 2
        await message.answer(f"Квадрат числа: {square}")
    else:
        await message.answer(message.text)


if __name__ == '__main__':

    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)