import telebot

bot = telebot.TeleBot('1700544454:AAG1uacjt9jg4Cyaaom4bYyyufEgYx2vNQU', parse_mode=None)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Привет, я Умный Помощник ребят из МТС СтартапХаб.\n"
                          "\n" 
                          "Моя задача - знать в лицо всех наших всех наших выпускников и быть с ними постоянно на связи;) "
                          "Время от времени я буду спрашивать тебя о состоянии твоей компании и интересоваться самыми интересными новостями. "
                          "Уверен, тебе будет, чем поделиться!"
                          "\n"
                          "\n"
                          "Со своей стороны, я постараюсь найти для тебя самые интересные возможности для сотрудничества с МТС и АФК Система. "
                          "\n"
                          "\n"
                          "Теперь давай наконец-то познакомимся! Как тебя зовут?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
