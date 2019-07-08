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

cmds = {'weather': 'Погода \U000026C5',
        'forecast': 'Прогноз \U0001F4C5',
        'help': 'Помощь \U00002753'}


@bot.message_handler(commands=['start', 'help'])
def info_action(msg):
    bot.send_message(msg.from_user.id, templates['info'],
                     reply_markup=markups.main, parse_mode='MarkDown')


@bot.message_handler(func=lambda msg: msg.text == cmds['weather'])
def weather_action(msg):
    msg = bot.send_message(msg.from_user.id, templates['geoPosition'], reply_markup=markups.remove)
    bot.register_next_step_handler(msg, geo_position_action)


def geo_position_action(msg):
    bot.send_message(msg.from_user.id, templates['weather'], reply_markup=markups.main)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True)
