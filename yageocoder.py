import requests as req

CONST_URL = 'https://geocode-maps.yandex.ru/1.x/?'


class GeoCoder:
    def __init__(self, apikey, url=CONST_URL):
        self.apikey = apikey
        self.url = url

    def is_exist(self, place):
        res = req.get(self.url, params={'apikey': self.apikey,'geocode': place, 'format': 'json'}).json()
        if res['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'] == '0':
            answer = {'existence': False}
            return answer
        else:
            answer = {'existence': True, 'object': res}
            return answer

    def get_coordinates(self, place):
        answer = self.is_exist(place)
        if answer['existence']:
            res = answer['object']
            position = res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            coordinates = [float(i) for i in position.split()]
            current_location = res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
                'GeocoderMetaData']['text']
            result = {'flag': True, 'lon': coordinates[1], 'lat': coordinates[0], 'location': current_location}
            return result
        else:
            result = {'flag': False}
            return result


