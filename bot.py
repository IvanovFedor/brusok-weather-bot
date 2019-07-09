import telebot
from json import load
import markups
import yageocoder
import openweather
from templates import templates
apikeys = load(open('apikeys.json', 'r'))

bot = telebot.TeleBot(apikeys['TeleBot'])

cmds = {'weather': 'Погода \U000026C5',
        'forecast': 'Прогноз \U0001F4C5',
        'help': 'Помощь \U00002753'}


@bot.message_handler(commands=['start', 'help'])
def info_action(msg):
    bot.send_message(msg.from_user.id, templates['info'],
                     reply_markup=markups.main, parse_mode='MarkDown')


@bot.message_handler(func=lambda msg: msg.text == cmds['weather'])
def weather_start(msg):
    msg = bot.send_message(msg.from_user.id, templates['geoposition'],
                           reply_markup=markups.remove, parse_mode='MarkDown')
    bot.register_next_step_handler(msg, weather_end)


def weather_end(msg):
    g = yageocoder.GeoCoder(apikeys['YaGeoCoder'])
    geocode = g.get_coordinates(msg.text)
    if not geocode['flag']:
        msg = bot.reply_to(msg, "Попробуйте еще раз",
                           parse_mode='MarkDown')
        bot.register_next_step_handler(msg, weather_end)
        return
    w = openweather.OpenWeather(apikeys['OpenWeather'])
    res = w.weather(geocode['lon'], geocode['lat'])

    text = templates['weather'].format(
        place=geocode['location'], weather=res['weather'][0]['description'],
        temp=res['main']['temp'], min_temp=res['main']['temp_min'],
        max_temp=res['main']['temp_max'], wind=res['wind']['speed'],
        clouds=res['clouds']['all'])

    bot.send_message(msg.from_user.id, text, parse_mode='MarkDown', reply_markup=markups.main)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True)
