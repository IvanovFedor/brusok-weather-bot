import telebot
from json import load
import markups
import telegramfont as font

apikeys = load(open('apikeys.json', 'r'))

bot = telebot.TeleBot(apikeys['TeleBot'])


@bot.message_handler(commands=['start', 'help'])
def info_action(msg):
    bot.send_message(msg.from_user.id, font.bold("Текст с помощью"),
                     reply_markup=markups.main, parse_mode='MarkDown')


bot.polling(none_stop=True)
