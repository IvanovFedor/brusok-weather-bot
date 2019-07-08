import telebot
from json import load
import markups

apikeys = load(open('apikeys.json', 'r'))

templates = {'info': '''
Интересует погода?
Просто отправь мне одну из этих команд:

*Погода* \U000026C5 на текущую дату и время
*Прогноз* \U0001F4C5 на следующие 3 дня
*Помощь* \U00002753
                     ''',
             'geoPosition': '''Шаг с геопозицией''',
             'weather': '''Типо погода''',
             'forecast': '''Типо прогноз'''}

bot = telebot.TeleBot(apikeys['TeleBot'])

# @bot.message_handler(content_types=['text'])
# # def weather_action(msg):
# #     msg = bot.send_message(msg.from_user.id, templates[''])


@bot.message_handler(commands=['start', 'help'])
def info_action(msg):
    bot.send_message(msg.from_user.id, templates['info'],
                     reply_markup=markups.main, parse_mode='MarkDown')


bot.polling(none_stop=True)
