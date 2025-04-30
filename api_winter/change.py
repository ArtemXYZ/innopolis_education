import asyncio
from io import BytesIO
# from PIL import Image
import re

import aiohttp

from api_winter.aiohttp_session import RESTAsyncRequest
# -------------------------------- Локальные модули
from configs import API_WEATHER


# ----------------------------------------------------------------------------------------------------------------------
class Winter:
    def __init__(self, api_token):

        self.api_token = api_token
        self.aiohttp_session = RESTAsyncRequest()
        # Маппинг иконок погоды на эмодзи
        self.icon_to_emoji = {
            '01d': '☀️', '01n': '🌑',  # ясное небо
            '02d': '🌤', '02n': '🌥',  # немного облачно
            '03d': '☁️', '03n': '☁️',  # облачно
            '04d': '🌥', '04n': '🌥',  # очень облачно
            '09d': '🌧', '09n': '🌧',  # дождь
            '10d': '🌦', '10n': '🌧',  # сильный дождь
            '11d': '⛈', '11n': '⛈',  # гроза
            '13d': '❄️', '13n': '❄️',  # снег
            '50d': '🌫', '50n': '🌫',  # туман
        }

    @staticmethod
    async def get_icon(icon: str):
        """
            Получаем URL-строку иконки от сервера по идентификатору из json
            01n.png -> 01d
        """

        # Используем регулярное выражение для замены 'n' на 'd'
        icon_new = re.sub(r'n', 'd', icon)
        url_icon = (f'https://openweathermap.org/img/wn/{icon_new}@2x.png')

        # async with aiohttp.ClientSession() as session:
        #     async with session.get(url_icon) as response:
        #
        #         icon_data = await response.read()
        #         icon_png = Image.open(BytesIO(icon_data))
        #
        #         # Сохранение изображения в байтовый поток
        #         img_byte_arr = BytesIO()
        #         icon_png.save(img_byte_arr, format='PNG')
        #         img_byte_arr.seek(0)
        #
        # return img_byte_arr
        return url_icon

    async def get_icon_emoji(self, icon: str):
        """
        Получаем соответствующий эмодзи для иконки погоды
        """
        icon_emoji = self.icon_to_emoji.get(icon, '')
        return icon_emoji

    async def get_country_coordinate(self, input_city_name, input_limit=None):
        """
            Узнаем координаты и код страны для города
            # :param api_weather: API ключ для OpenWeatherMap
            :param input_city_name: Название города
            :param input_limit: Лимит результатов (по умолчанию 1)
            :return: Координаты и код страны
        """

        if input_limit is None:

            url = (f'http://api.openweathermap.org/geo/1.0/direct?q={input_city_name}&appid={self.api_token}')

        else:

            url = (
                f'http://api.openweathermap.org/geo/1.0/direct?q={input_city_name}'
                f'&limit={input_limit}&appid={self.api_token}'
            )

        data = await self.aiohttp_session.get_async_response(url)

        if data:

            return data[0]['lat'], data[0]['lon'], data[0].get('country')
        else:
            print("Город не найден")
            return None, None, None

            # raise ValueError("Город не найден")

    async def get_weather_by_coordinate(self, lat, lon, url_type_prognosis: str):
        """
            Узнаем погоду по координатам.

            :param lat: Широта
            :param lon: Долгота
            :param API_WEATHER: API ключ для OpenWeatherMap
            :return: Данные о погоде

            metric  - units	необязательно	Доступны единицы измерения. standard, metric и imperial единицы измерения.
            cnt - Чтобы ограничить количество временных меток в ответе API, пожалуйста, настройте cnt.

        """

        # По условию выдаем тип url для получения различного рода прогноза, возвращаем json

        if url_type_prognosis == 'now':  # Прогноз сейчас +

            url = (
                f'https://api.openweathermap.org/data/2.5/weather?lat={lat}'
                f'&lon={lon}&appid={self.api_token}&units=metric'
            )

        elif url_type_prognosis == '5day':  # Прогноз на 5 дней с разбивкой по 3 часа + (в нашем варианте = 48 часов).

            # Запрос по этому URL возвращает прогноз погоды с часовым интервалом на ближайшие 48 часов и текущие данные,
            # исключая данные по минутам и ежедневные прогнозы.
            url = (f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,'
                   f'daily&appid={self.api_token}&units=metric')

        data = await self.aiohttp_session.get_async_response(url)
        return data

    # Выдать погоду (json на выходе)
    async def get_weather(self, input_city_name, url_type_prognosis: str = 'now'):
        # try:

        # 1. Получаем координаты города
        lat, lon, country_code = await self.get_country_coordinate(input_city_name, input_limit=1)

        # print(f'lat, lon, country_code: {lat}, {lon}, {country_code}')

        # Получаем прогноз в json
        weather_data = await self.get_weather_by_coordinate(lat, lon, url_type_prognosis)
        return weather_data

        # except Exception as e:
        #     print(f'Ошибка : {e}')
