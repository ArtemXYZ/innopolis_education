"""
    pass
"""

import re
import xmltodict

from asincs.aiohttp_session import RESTAsyncRequest


# ======================================================================================================================
class SitemapHandler:
    """
        Класс содержит методы получения и обработки данных из sitemaps mvideo.
        https://www.mvideo.ru/sitemaps/sitemap-categories-www.mvideo.ru-1.xml.
    """

    def __init__(self, arq: RESTAsyncRequest):
        self._arq = arq

    @staticmethod
    async def pars_sitemap_xml(xml_data: bytes) -> [str, ...]:
        """
            Вспомогательный метод для обработки данных из xml.

            Внутри используется преобразование xml в словарь с вложенными словарями.
                example = {
                    'urlset':
                        {
                            '@xmlns': 'http://www.sitemaps.org/schemas/sitemap/0.9',
                            '@xmlns:news': 'http://www.google.com/schemas/sitemap-news/0.9',
                            '@xmlns:xhtml': 'http://www.w3.org/1999/xhtml',
                            '@xmlns:image': 'http://www.google.com/schemas/sitemap-image/1.1',
                            '@xmlns:video': 'http://www.google.com/schemas/sitemap-video/1.1',

                            'url': [
                                {
                                    'loc': 'https://www.mvideo.ru/sadovaya-tehnika-i-oborudovanie-8027/sadovye-\
                                        telezhki-33570',
                                    'lastmod': '2025-02-07', 'changefreq': 'daily', 'priority': '0.5'
                                },
                                {
                                    'loc': 'https://www.mvideo.ru/sadovaya-tehnika-i-oborudovanie-8027/\
                                        sadovyi-dekor-33716',
                                    'lastmod': '2025-02-07', 'changefreq': 'daily', 'priority': '0.5'
                                },
                            ]
                        }
            Логика: получаем ссылки все с содержанием категорий. Через регулярное выражение отбираем вхождения цифр
            (id категорий), при этом отфильтровываем ссылки с содержанием категорий по установке (они не дают результат,
            мусорные). Далее после получения результатов у нас имеется список с дубликатами категорий, тк в каждой
            ссылке дублируются главная категория и подкатегории. Что бы устранить дубликаты, добавляем этот список
            в сет с результатами, происходит удаление дубликатов.

        """

        results: set = set()
        # Ссылки попавшие под фильтрацию:
        filter_out: set = set()

        # Паттерны регулярных выражений для поиска подстроки в ссылках.

        # Ищет цифры, начинающиеся с дефиса, отбирает только цифры, игнорируя дефис в результате поиска:
        # + проверяет, что за числом следует либо символ /, либо конец строки и игнорирует такие вхождения.
        main_pattern = re.compile(r'(?<!-)-(\d+)(?=/|$)')  # r'\d+'  # r'(?<!-)-\d+' # r'(?<!-)-(\d+)'
        # Ищет вхождения со словом "ustanovka":
        sub_pattern = re.compile(r'\bustanovka\b')

        # Преобразование XML в словарь
        xml_content = xmltodict.parse(xml_data)

        try:
            # Извлекаем основной контейнер с информацией:
            data_list_dict: list[dict, ...] = xml_content['urlset']['url']

        except KeyError as e:
            raise ValueError(
                f'Ошибка извлечения данных при попытке обращении к ключам (dict / list) '
                f'преобразованного xml (Lib: "xmltodict") {e}'
            )

        for data_dict in data_list_dict:

            data_row = data_dict.get('loc')

            if data_row:
                if sub_pattern.search(data_row):
                    filter_out.update(data_row)  # Устарело, заменяем на сеты  append(data_row)
                    # print('Пропуск ссылки с содержанием категории ("ustanovka") ')
                    continue

                # Парсим все айди в урл строке:
                # id_list = re.findall(r'\d+', data_row) # Устарело, замена на более производительное (ниже).
                # Использование re.compile имеет смысл в случаях многократно использования одно и то же рег-выражения:
                id_list: list = main_pattern.findall(data_row)
                # print(id_list)

                # results_temp: set = results_temp + id_list # Устарело, замена на более производительный set.
                results.update(id_list)

        # print(f'Ссылки попавшие под фильтрацию: {filter_out}')

        return list(results)

    async def get_categories_id_from_sitemap(self) -> set:
        """
            Метод получает данные со страницы:

                * https://www.mvideo.ru/sitemaps/sitemap-categories-www.mvideo.ru-1.xml
            и обрабатывает все id категорий, содержащихся в url-строке, учитывая сложную логику обработки.
            Для того что бы корректно работать дальше с данными в данном методе на выходе имеются только уникальные id,
            также пропускается одна категория "Установка" - она не дает результатов.
        """

        url_sitemap = 'https://www.mvideo.ru/sitemaps/sitemap-categories-www.mvideo.ru-1.xml'

        # Получаем ответ в виде байтов:
        # _xml_byte_data: bytes = self._get_response_json(url_sitemap, mode='bytes')  # text / bytes
        _xml_byte_data: bytes = await self._arq.get_no_disconnect_request(url=url_sitemap, mode='bytes')

        # Получаем все категории (categories_ids) с сайт-мап, [str, ...]:
        _ids: set = await self.pars_sitemap_xml(_xml_byte_data)

        return _ids
