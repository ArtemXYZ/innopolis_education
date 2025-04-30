"""
    pass
"""

import asyncio
import time

import csv
from googletrans import Translator

from api_winter.change import Winter
from api_winter.configs import API_WEATHER


# from api_winter.translator import translate_from_language


# ==============================================================================
class WinterManager:
    def __init__(self):
        self.api_token = API_WEATHER
        self.winter = Winter(self.api_token)
        self.translator = Translator()

    async def translate_from_language(self, input_text: str, input_dest: str):
        """
            Определить язык пользователя по координатам по вводу.

            :param input_dest:'ru'
            :return:
        """

        result = await self.translator.translate(text=input_text, dest=input_dest)

        return result.text

    async def get_winter_data(self, city):
        """
            pass
        """

        city_name_eng = await self.translate_from_language(city, 'en')

        # print(f'city_name_eng: {city_name_eng}')

        if city_name_eng is None:
            raise ValueError('Ошибка, не удалось получить данные о городе.')

        data = await self.winter.get_weather(input_city_name=city_name_eng)

        # print(f'data: {data}')

        if not data:
            raise ValueError('Ошибка, не удалось получить данные о погоде.')

        # Интерпретатор:
        weather_description = data['weather'][0]['description']

        weather_description_original = await self.translate_from_language(weather_description, 'ru')

        try:
            temperature = data['main']['temp']
            # feels_like = data['main']['feels_like']
            # temp_min = data['main']['temp_min']
            # temp_max = data['main']['temp_max']
            # pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            # clouds = data['clouds']['all']
        except KeyError as error:
            raise KeyError(f'Ошибка доступа к данным, не существует ключа {error}')

        # Состав: температура, влажность, скорость ветра и общее описание погоды
        weather_report_dict = {
            'city': city,
            'temperature': temperature,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'weather_description_original': weather_description_original,
        }

        weather_report_tuple = (city, temperature)

        return weather_report_dict, weather_report_tuple

    async def run_search_city_winter(self):
        """
            pass
        """

        w_list = []
        tuple_for_analysis_list = []

        # Выполняем перевод для требуемых городов (в соответствии с докум.)
        city_name_no_translate = ["Москва", "Нью-Йорк", "Токио", "Лондон", "Берлин"]

        for city in city_name_no_translate:
            dict_w, tuple_for_analysis = await self.get_winter_data(city)

            w_list.append(dict_w)
            tuple_for_analysis_list.append(tuple_for_analysis)

        print('w_list', w_list)
        print('tuple_for_analysis_list', tuple_for_analysis_list)

        return w_list, tuple_for_analysis_list

    @staticmethod
    async def analysis(tuple_list_city_temper: list[tuple]):
        """
            Найдите среднюю температуру среди всех городов.
            Определите город с самой высокой и самой низкой температурой.
            Выведите на экран результирующие данные
        """
        if not tuple_list_city_temper:
            raise ValueError("Список городов пуст")

        total_temp = 0
        min_temp = float('inf')  # Инициализируем очень большим значением
        max_temp = float('-inf')  # Инициализируем очень маленьким значением
        min_city = ""
        max_city = ""

        for city, temperature in tuple_list_city_temper:
            total_temp += temperature

            if temperature > max_temp:
                max_temp = temperature
                max_city = city

            if temperature < min_temp:
                min_temp = temperature
                min_city = city

        avg_temp = total_temp / len(tuple_list_city_temper)

        print(f'Средняя температура среди всех городов: {avg_temp:.1f}°C')
        print(f'Город с самой высокой температурой: {max_city} ({max_temp:.1f}°C)')
        print(f'Город с самой низкой температурой: {min_city} ({min_temp:.1f}°C)')

        return avg_temp, min_temp, max_temp

    @staticmethod
    async def save_to_csv(data: list[dict], filename: str = 'weather_data.csv'):
        """
        Сохраняет полные данные о погоде в CSV файл
        :param data: Список словарей с полными данными о погоде
        :param filename: Имя файла для сохранения
        """
        if not data:
            print("Нет данных для сохранения")
            return

        # Автоматически определяем заголовки из ключей первого словаря
        fieldnames = list(data[0].keys())

        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()  # Записываем заголовки
                writer.writerows(data)  # Записываем данные

            print(f"Данные успешно сохранены в файл {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении в CSV: {e}")

    async def main(self):
        """
            pass
        """

        # Основные данные:
        w_list, tuple_list_city_temper = await self.run_search_city_winter()

        # Сохранение w_list:
        await self.save_to_csv(data=w_list)

        # Анализ tuple_list_city_temper:
        await self.analysis(tuple_list_city_temper)


if __name__ == '__main__':
    asyncio.run(WinterManager().main())
