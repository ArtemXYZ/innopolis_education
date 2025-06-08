import pandas as pd

# Инициализация счетчиков
weekend_rentals = 0
weekday_rentals = 0

# 1. ======================================== Загрузка данных

# Правильный способ чтения CSV - через pd.read_csv()
df = pd.read_csv('../data/day.csv')  # Убедитесь, что файл day.csv находится в рабочей директории

# 2. ======================================== Вывод первых 5 строк
print("Первые 5 строк DataFrame:\n")
print(df.head())  # Используем объект df, а не класс DataFrame

# 3. ======================================== Проверка названий столбцов
print("Названия столбцов:\n")
print(df.columns)  # Аналогично - работаем с экземпляром df

# 4. ======================================== Проверка пропущенных значений
print("Пропущенные значения:\n")
print(df.isnull().sum())

# 5. ======================================== Итерирование по строкам с помощью iterrows()
for index, row in df.iterrows():
    if row['weekday'] in [0, 6]:  # 0 - воскресенье, 6 - суббота в этом DataFrame
        weekend_rentals += row['cnt']
    else:
        weekday_rentals += row['cnt']

print("Общее количество аренд:\n")
print(f"Выходные дни: {weekend_rentals}")
print(f"Будние дни: {weekday_rentals}")

# 6. ======================================== Преобразование категориальных переменных
# Создаем срез датафрейма с категориальными признаками
category_df = df[['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit']].copy()  #

# Добавляем числовые представления (они уже есть в датафрейме)
category_df['numerical_value'] = category_df.values.tolist()

# Выводим первые 10 строк нужных колонок
print(category_df.head(10))

# 7. ======================================== Группировка данных по месяцам:
# Преобразуем колонку dteday в datetime если это еще не сделано
df['dteday'] = pd.to_datetime(df['dteday'])

# Группировка по месяцам и подсчет среднего количества аренд
monthly_avg = df.groupby(df['dteday'].dt.month)['cnt'].mean()

print("Среднее количество аренд по месяцам:\n")
print(monthly_avg.to_frame().rename(columns={'cnt': 'Среднее количество аренд'}))

# 8. ======================================== Обработка пропущенных значений:
# Проверяем пропущенные значения еще раз
print("\nПроверка пропущенных значений перед обработкой:")
print(df.isnull().sum())

# Заполнение пропущенных значений средним (если они есть)
for column in df.columns:
    if df[column].isnull().any():
        if df[column].dtype in ['int64', 'float64']:
            df[column].fillna(df[column].mean(), inplace=True)
        else:
            # Для нечисловых данных можно использовать моду
            df[column].fillna(df[column].mode()[0], inplace=True)

# Альтернативный вариант - удаление строк с пропусками
# df.dropna(inplace=True)

print("\nПроверка пропущенных значений после обработки:")
print(df.isnull().sum())

