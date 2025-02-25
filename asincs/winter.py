"""
    pass
"""

from asincs.aiohttp_session import RESTAsyncRequest


class Winter:

    def __init__(self):
        self._arequest = RESTAsyncRequest()

    # Устанавливаем адрес запроса

    async def decode_address(self, input_address: str):
        """
        Пример ответа:
            response = [
                {
                    'place_id': 187265215, # id места.
                    'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright',
                    'osm_type': 'relation',
                    'osm_id': 377931,

                    'lat': '52.6664095', # Широта
                    'lon': '52.3978605', # Долгота

                    'class': 'waterway | building | shop',
                    'type': 'river | apartments | convenience | administrative', # Судоходный или нет.
                    'place_rank': 18, # Место в рейтинге.
                    'importance': 0.4758467396969812, # важность\\значение
                    'addresstype': 'river | building | village',   # Тип адреса.

                    'name': 'Самара',  # Имя города.
                    'display_name': 'Самара, Приволжский федеральный округ, Россия', # Адрес.

                    'boundingbox': ['51.8717949', '53.2426759', '50.0315666', '54.5019218']},  # Территориальные границы.
                },
            ]

            latitude = data[0]['lat']  # Широта
            longitude = data[0]['lon']  # Долгота
            longitude = data[0]['name']  # Имя города.
            longitude = data[0]['display_name']  # Адрес.



            В ответе может присутствовать несколько вариантов (все совпадения по имени города например).
            По этому, ответ будет возвращен в таком виде:
            {6: ('16.4066851', '120.3327898', 'Samara', 'Samara, Aringay, La Union, Ilocos Region, 2503, Pilipinas')},
            {7: ('9.8834197', '-85.5288998', 'Sámara', 'Sámara, Cantón de Nicoya, Guanacaste, 50205, Costa Rica')},
            {8: ('52.6664095', '52.3978605', 'Самара', 'Самара, Приволжский федеральный округ, Россия')},
            {9: ('48.5354317', '36.0283512', 'Самара', 'Самара, Україна')},
            {10: ('40.8863071', '39.8573871', 'Gülyurdu', 'Gülyurdu, Yomra, Trabzon, Karadeniz Bölgesi, Türkiye')}
            ]
            Это сделано,для того что бы в боте можно было легко обращаться по номеру ответа (по ключу) и возвращать картеж
            отобранных данных.

        """

        response_parts_list = []

        url = f"https://nominatim.openstreetmap.org/search?format=json&q={input_address}"
        data = await self._arequest.get_no_disconnect_request(url)  # Делаем GET запрос к API Nominatim
        print(data)

        if data:

            for numb, response_variant in enumerate(data, 1):

                latitude = response_variant['lat']  # Широта
                longitude = response_variant['lon']  # Долгота
                city_name = response_variant['name']  # Имя города \ Организации (магазин или другое по адресу).
                autput_address = response_variant['display_name']  # Адрес.

                response_part = {numb: (latitude, longitude, city_name, autput_address)}
                response_parts_list.append(response_part)

                break # Служебный

        print(f'По запросу "{input_address}" получены результаты: ')
        print(response_parts_list)

        return response_parts_list