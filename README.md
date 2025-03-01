## Запуск бота
```
pip install - r requirements.txt
python bot.py
```
TestBot – это простой Telegram-бот, который может отвечать на сообщения пользователей, предоставлять список команд и генерировать случайные числа. Он создан с использованием библиотеки Aiogram .

```
@dp.callback_query()
async def callback_handler(callback: types.CallbackQuery):
    if callback.data =="start" :
      await callback.message.answer("Напиши  /start , что бы начать работу с ботом")
    elif callback.data =="help" :
         await callback.message.answer("Альтернативная помощь или напиши /help")
    elif callback.data =="random" :
        await callback.message.answer("Хочешь рандомное число? напиши: /random")
```
