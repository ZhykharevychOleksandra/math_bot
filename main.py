import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from config import TOKEN
import random

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Hello! I'm a math bot\n" 
        "I can: \n" 
        "- calculate examples\n"
        "- give you problems\n")
    
@dp.message(Command("help"))
async def help_handler(message: types.Message):
    await message.answer(
        "Commands:\n" 
        "/calc — calculator\n" 
        "/math — problem\n" 
        "/help — help\n")
    
@dp.message(Command("calc"))
async def calc_handler(message: types.Message):
    await message.answer("Enter an example (e.g. 2 + 2):")


correct_answer = None
@dp.message(Command("math"))
async def math_handler(message: types.Message):
    global correct_answer

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    correct_answer = num1 * num2

    await message.answer(f"How much will be: {num1} * {num2}?")

@dp.message()
async def handle_all(message: types.Message):
    global correct_answer

    text = message.text

    if correct_answer is not None:
        if text.isdigit():
            if int(text) == correct_answer:
                await message.answer("Correct!")
            else:
                await message.answer(f"Wrong, correct answer: {correct_answer}")

            correct_answer = None
            return

    try:
        text = message.text.replace(" ", "")
       
        if "+" in text:
            num1, num2 = text.split("+")
            result = int(num1) + int(num2)
            
        elif "-" in text:
            num1, num2 = text.split("-")
            result = int(num1) - int(num2)
        
        elif "*" in text:
            num1, num2 = text.split("*")
            result = int(num1) * int(num2)
            
        elif "/" in text:
            num1, num2 = text.split("/")
            result = int(num1) / int(num2)
        else:
            await message.answer("Unknown operator")
            return
        
        await message.answer(f"Result: {result}")

    except:
        await message.answer("Enter an example (e.g. 2 + 2):")
         
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

