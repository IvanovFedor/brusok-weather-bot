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
    bot.reply_to(msg, templates['info'],
                 reply_markup=markups.main, parse_mode='MarkDown')


@bot.message_handler(func=lambda msg: msg.text == cmds['help'])
def help_action(msg):
    bot.reply_to(msg, templates['help'],
                 reply_markup=markups.main, parse_mode='MarkDown')


@bot.message_handler(func=lambda msg: msg.text == cmds['weather'])
def weather_start(msg):
    msg = bot.reply_to(msg, templates['geoposition'],
                       reply_markup=markups.main, parse_mode='MarkDown')
    bot.register_next_step_handler(msg, weather_end)


def weather_end(msg):
    g = yageocoder.GeoCoder(apikeys['YaGeoCoder'])
    geocode = g.get_coordinates(msg.text)
    if not geocode['flag']:
        msg = bot.reply_to(msg, templates['error'],
                           parse_mode='MarkDown')
        bot.register_next_step_handler(msg, weather_end)
        return
    w = openweather.OpenWeather(apikeys['OpenWeather'])
    res = w.weather(geocode['lat'], geocode['lon'])

    text = templates['weather'].format(
        place=geocode['location'], weather=res['weather'][0]['description'],
        temp=res['main']['temp'], min_temp=res['main']['temp_min'],
        max_temp=res['main']['temp_max'], wind=res['wind']['speed'],
        clouds=res['clouds']['all'])

    bot.reply_to(msg, text, parse_mode='MarkDown',
                 reply_markup=markups.main)


@bot.message_handler(func=lambda msg: msg.text == cmds['forecast'])
def forecast_start(msg):
    msg = bot.reply_to(msg, templates['geoposition'],
                       reply_markup=markups.remove, parse_mode='MarkDown')
    bot.register_next_step_handler(msg, forecast_end)


def forecast_end(msg):
    g = yageocoder.GeoCoder(apikeys['YaGeoCoder'])
    geocode = g.get_coordinates(msg.text)
    if not geocode['flag']:
        msg = bot.reply_to(msg, templates['error'],
                           parse_mode='MarkDown')
        bot.register_next_step_handler(msg, forecast_end)
        return
    w = openweather.OpenWeather(apikeys['OpenWeather'])
    res = w.forecast_limited(geocode['lat'], geocode['lon'], 3)

    text = templates['forecast'].format(place=geocode['location'])
    for day in res['list']:
        text += templates['forecast_component'].format(
            date=day['dt_txt'].split()[0], weather=day['weather'][0]['description'],
            temp=day['main']['temp'], wind=day['wind']['speed'], clouds=day['clouds']['all'])

    bot.reply_to(msg, text, parse_mode='MarkDown',
                 reply_markup=markups.main)


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()
bot.polling(none_stop=True)
