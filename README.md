### Telebot ###
## ItakinRovodis_testbot ##

Чего греха таить - использовалась документация https://pypi.org/project/pyTelegramBotAPI/
Ctrl + C 
Ctrl + V

> bot.message_handler(commands=['start', 'help'])
> def send_welcome(message):
>	bot.reply_to(message, "Привет, Крошка!")

Это наше приветствие - со стандартными для ботов кнопками: старта и помощи

>bot.message_handler(func=lambda m: True)
>def echo_all(message):
>	bot.reply_to(message, message.text)

Отвечаем на любое сообщение текстом самого сообщения - всё в общем-то просто

> bot.infinity_polling()

Просто заставляем работать, пока сами не остановим.
Всё!