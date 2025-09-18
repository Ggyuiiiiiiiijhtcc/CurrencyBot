import aiohttp
import os
from aiogram import Router
from aiogram.filters import CommandStart,Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from dotenv import load_dotenv

load_dotenv()
router = Router()

class Change(StatesGroup):
    first_currency = State()
    second_currency = State()
    amount = State()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer('Бот показывает, актуальные новости курса валют!')

@router.message(Command('Convert'))
async def convert_start(message: Message, state: FSMContext):
    await message.answer("Введите валюту, из которой хотите конвертировать (например USD):")
    await state.set_state(Change.first_currency)

@router.message(Change.first_currency)
async def first_currency (message: Message, state: FSMContext):
    await state.update_data(first_currency= message.text.upper())
    await message.answer('Введите валюту, из которой хотите конвертировать (например UAH):')
    await state.set_state(Change.second_currency)

@router.message(Change.second_currency)
async def second_currency (message: Message, state: FSMContext):
    await state.update_data(second_currency= message.text.upper())
    await message.answer('Введите сумму для конвертации:')
    await state.set_state(Change.amount)

@router.message(Change.amount)
async def amount_input (message: Message, state: FSMContext):
    try:
        amount = float(message.text)
        if amount <= 0:
            raise ValueError
    except ValueError:
        await message.answer('Пожалуйста, введите корректное число.')
        return
    date = await state.get_data()
    firsts_currency = date['first_currency']
    seconds_currency = date['second_currency']

    url = 'https://api.exchangerate.host/convert'
    params = {
             "access_key" : os.environ.get('API_KEY'),
             "from": firsts_currency,
             "to": seconds_currency,
             "amount": amount
         }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            if resp.status != 200:
                await message.answer("Ошибка при получении данных")
                await state.clear()
                return
            result_data = await resp.json()

    result = result_data['result']
    if result is None:
        await message.answer('Не удалось конвертировать. Проверьте валюты.')
        await state.clear()
        return
    round_ded = round(result, 2)
    await message.answer(f'{amount} {firsts_currency} = {round_ded} {seconds_currency}')
    await state.clear()



@router.message(Command('ChangeInfo'))
async def changeinfo(message: Message):
    if not os.environ.get('API_KEY'):
        await message.answer("Не установлен API_KEY")
        return

    url = 'https://api.exchangerate.host/live'
    params = {
        "access_key": os.environ.get('API_KEY'),
        "base": "USD",
        "currencies": "EUR,PLN,RUB,UAH"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            if resp.status != 200:
                await message.answer('Ошибка при получении валют')
                return
            data = await resp.json()

    rates = data.get("quotes", {})
    if not rates:
        await message.answer('Не удалось показать актуальный курс валют')
        return

    currencies_codes = ["EUR", "PLN", "RUB", "UAH"]
    currencies_names = {"EUR": "Евро",
                        "PLN": "Злотый",
                        "RUB": "Рубли",
                         "UAH": "Гривна"}

    text_lines = []
    for code in currencies_codes:
        rate = rates.get(f"USD{code}")
        if rate is not None:
            rate = round(rate, 2)
            text_lines.append(f"Доллар -> {currencies_names[code]} : {rate}")

    text = "\n".join(text_lines)
    await message.answer(f"Вот актуальный курс валют:\n{text}")



