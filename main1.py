import asyncio
from aiogram import Bot, Dispatcher, executor
from config import TOKEN
loop = asyncio.get_event_loop()
bot = Bot (TOKEN, parse_mode="HTML")#<i>Italic</i>, <b>Bold</>
dp = Dispatcher (bot, loop=loop)
if name == "__main1__":
    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)

