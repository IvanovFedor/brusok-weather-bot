import requests as req

CONST_URL = 'https://geocode-maps.yandex.ru/1.x/?'


class GeoCoder:
    def __init__(self, apikey, url=CONST_URL):
        self.apikey = apikey
        self.url = url


    def get_coordinates(self, place):
        res = req.get(self.url, params=dict(apikey=self.apikey, geocode=place, format='json')).json()
        if res['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'] == '0':
            result = {'existence': False}
            return result
        else:
            position = res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            coordinates = [float(i) for i in position.split()]
            current_location = res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
                'GeocoderMetaData']['text']
            result = {'existence': True, 'lon': coordinates[1], 'lat': coordinates[0], 'location': current_location}
            return result

    def get_place(self, lat, lon):
        res = req.get(self.url, params=dict(apikey=self.apikey, geocode=str(lat) + ', ' + str(lon), sco='latlong',
                                            format='json')).json()
        current_location = res['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['text']
        result = {'existence': True, 'location': current_location}
        return result

