import requests as req
from datetime import datetime

CONST_URL = 'http://api.openweathermap.org/data/2.5/{method}'


class OpenWeather:
    def __init__(self, apikey, url=CONST_URL):
        self.url = url
        self.apikey = apikey

    def weather(self, lat, lon, units='metric', lang='ru'):
        res = req.get(self.url.format(method='weather'), params={'appid': self.apikey, 'lat': lat,
                                                     'lon': lon, 'units': units, 'lang': lang})
        return res.json()

    def forecast(self, lat, lon, count=40, units='metric', lang='ru'):
        res = req.get(self.url.format(method='forecast'), params={'appid': self.apikey, 'lat': lat,
                                                          'lon': lon, 'cnt': count,
                                                          'units': units, 'lang': lang})
        return res.json()

    def forecast_limited(self, lat, lon, day_count, units='metric', lang='ru'):
        today = 8 - datetime.today().hour // 3  # количество записей на текущюю дату

        res = self.forecast(lat, lon, today + day_count * 8, units, lang)
        # today + day_count * 8 (кол-во записей на текущюю дату + 8 записей/день * кол-во дней

        res['list'] = res['list'][today + 5::8]  # берем только записи последующих дней на 15.00
        res['cnt'] = day_count  # обновляем количество записей
        return res

