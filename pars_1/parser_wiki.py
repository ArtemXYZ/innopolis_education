"""
    Парсер заголовков третьего уровня (h3).
"""


import requests
from bs4 import BeautifulSoup


# URL страницы Википедии о Python
url = 'https://ru.wikipedia.org/wiki/Python'

# Отправляем GET-запрос к странице
response = requests.get(url)
response.raise_for_status()  # Проверяем, что запрос успешен

# Создаем объект BeautifulSoup для парсинга HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все заголовки третьего уровня (h3)
h3_headings = soup.find_all('h3')

# Извлекаем текст из каждого заголовка и убираем лишние пробелы
headings_text = [heading.get_text().strip() for heading in h3_headings]

# Сохраняем заголовки в текстовый файл
with open('python_wiki_h3_headings.txt', 'w', encoding='utf-8') as file:
    for heading in headings_text:
        file.write(heading + '\n')

print(f'Сохранено {len(headings_text)} заголовков h3 в файл python_wiki_h3_headings.txt')