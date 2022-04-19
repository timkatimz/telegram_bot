import telebot
from utils import shuffle_questions
bot = telebot.TeleBot("5237243824:AAFQd9dqsQSOWgByC3rreG_XaffuIewHC8A")
question = shuffle_questions()



@bot.message_handler(commands=["start"])
def start(message):
    user = f"Привет, <b>{message.from_user.first_name}</b>!"
    message_ = f"Функционал бота пока не большой. Мы можем предложить подборку книг для изучения " \
               "того или иного языка программирования. Подборки книг собраны на Яндекс.Диск\n\n" \
               "Для получения подборки просто отправьте мне название языка программирования\n" \
               "Помимо этого, у меня есть подборка книг для дизайнера (доступна по ключу дизайн), " \
               "и подборка книг для изучения Linux, сетей и протоколов, взлома и интернет безопасности"
    bot.send_message(message.chat.id, user, parse_mode="html")
    bot.send_message(message.chat.id, message_, parse_mode="html")




@bot.message_handler()
def get_library(message):
    if message.text.lower() in ["python"]:
        bot.send_message(message.chat.id, "https://disk.yandex.ru/d/VVCvBthXrYktTw")
    elif message.text.lower() in ["c++", "cplusplus"]:
        bot.send_message(message.chat.id, "https://disk.yandex.ru/d/71NCUawA-9BDEg")
    elif message.text.lower() in ["c#", "csharp", "c sharp"]:
        bot.send_message(message.chat.id, "https://disk.yandex.ru/d/dM9ZfTcedxFfhA")
    elif message.text.lower() in ["golang", "go"]:
        bot.send_message(message.chat.id, "https://disk.yandex.ru/d/_j086orPgJR5RQ")
    elif message.text.lower() == "java":
        bot.send_message(message.chat.id, "https://disk.yandex.ru/d/TjBU_v8LYc1xKA")
    elif message.text.lower() in ["javascript", "js", "react"]:
        bot.send_message(message.chat.id, "https://disk.yandex.ru/d/U257P6nAR4ct3A")
    elif message.text.lower() in ["дизайн", "design"]:
        bot.send_message(message.chat.id, "https://disk.yandex.ru/d/hJlp_SwVhwBJMA")
    elif message.text.lower() in ["linux", "kali", "взлом", "безопасность", "pentest"
                                  "сети", "протоколы"]:
        bot.send_message(message.chat.id, "https://disk.yandex.ru/d/iN2gp9azN1JpJQ")
    elif message.text.lower() in ["ans"]:
        bot.send_message(message.chat.id, question["a"], parse_mode='html')
    else:
        bot.send_message(message.chat.id, "Не знаю такого языка программирования")


bot.polling(non_stop=True)





















