import os
import random

from aiogram import Router, F
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile, MessageAutoDeleteTimerChanged

from states import LevelState
from keyboards import levels_btn, stop_btn

router = Router()

def get_min_max_number(level):
    # funksiyani qolgan lever uchun xam moslash kerak
    if level == "Level 1️⃣":
        return 1, 11
    elif level == "Level 2️⃣":
        return 10, 101

@router.message(CommandStart())
async def start_command(message: Message):

    image = FSInputFile(os.path.join(os.path.dirname(__file__), "images", "мемы-из-тиктока-энштейн.png"))
    from_user = message.from_user
    first_name = from_user.first_name
    last_name = from_user.last_name
    full_name = f"{first_name} {last_name if last_name else ''}"
    await message.answer(f"Salom {full_name}")
    await message.answer_photo(photo=image, caption=f"Xush kelibsiz {full_name}bilag'on, "
                                                    f"sizga bir nechta savollar berib "
                                                    f"bilimingizni tekshirib beramiz!", reply_markup=levels_btn)


@router.message(F.text == "Level 1️⃣")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(1, 11)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(1, 11)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="Level 1️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
    await state.set_state(LevelState.javob)

@router.message(F.text == "Level 2️⃣")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(11, 500)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(11, 500)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="Level 2️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
    await state.set_state(LevelState.javob)


@router.message(F.text == "Level 3️⃣")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(101, 2000)} {random.choice(['+', '-', '*'])}"
                f" {random.randint(101, 2000)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="Level 3️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
    await state.set_state(LevelState.javob)


@router.message(F.text == "Level 4️⃣")
async def level_1(message: Message, state: FSMContext):
    question = (f"{random.randint(100, 10000)} {random.choice(['/' '*'])}"
                f" {random.randint(100, 10000)}")
    answer = eval(question)
    await state.update_data(answer=answer, question=question, level="Level 4️⃣",
                            correct=0, incorrect=0)
    await message.answer(text=f"SAVOL: {question} = ?", reply_markup=stop_btn)
    await state.set_state(LevelState.javob)
