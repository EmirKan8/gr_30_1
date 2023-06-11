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



@dp.message_handler(Command('quiz'))
async def start_quiz(message: types.Message):
    await QuizState.QUESTION_1.set()
    await message.answer("Первый вопрос: В какому году был основан Geeks?")



@dp.message_handler(state=QuizState.QUESTION_1)
async def answer_question_1(message: types.Message, state: FSMContext):

    await message.answer("Второй вопрос: какое море не имеет берегов?")


    await QuizState.next("2018")


@dp.message_handler(state=QuizState.QUESTION_2)
async def answer_question_2(message: types.Message, state: FSMContext):

    await message.answer("Саргассово море")
    await state.finish("Молодец.Мегахорош")



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
