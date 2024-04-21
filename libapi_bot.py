import time

import telebot

token = '6994860528:AAFT6Lbbm0Rqftmp-ME6XuG3EG0oCwwppc0'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,'Чо надо')


@bot.message_handler(commands=['timer'])
def say(message):
    for i in range(5):
        time.sleep(1)
        bot.send_message(message.chat.id, i + 1)

@bot.message_handler(commands=['say'])
def say(message):
    text = ' '.join(message.text.split(' ')[1:])
    bot.reply_to(message,f'***{text.upper()}!***')
@bot.message_handler(content_types='text')
def reverse_text(message):
    if 'жопа' in message.text.lower():
        bot.reply_to(message, 'Текст содержит слово жопа')
        return
    text = message.text[::-1]
    bot.reply_to(message,text)


bot.polling()