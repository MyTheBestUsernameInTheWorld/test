import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from menu import register_handlers_menu

bot = Bot(token='5589827898:AAHr-s-UZbKe8IFGFvVDPs5_z87q9FlsWtk')  # ваш токен

dp = Dispatcher(bot, storage=MemoryStorage())


async def main():

    register_handlers_menu(dp)

    await dp.skip_updates()
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
