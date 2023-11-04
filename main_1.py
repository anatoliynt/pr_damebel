import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
import csv
from datetime import datetime

# Запросим у пользователя адрес сайта
url = input("Введите адрес сайта (например, https://mebel.com/): ")

try:
    # Отправляем GET-запрос к сайту
    response = requests.get(url)

    # Проверяем успешность подключения (код 200)
    if response.status_code == 200:
        print("Подключение успешно!")

        # Используем BeautifulSoup для парсинга HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Находим все блоки с классом "card__wrapper"
        card_wrappers = soup.find_all('div', class_='card__wrapper')

        # Создаем или открываем файл card__wrapper.html для записи результатов
        with open('Baza/card__wrapper.html', 'w', encoding='utf-8') as file:
            # Проходимся по каждому блоку и извлекаем ссылки
            for card_wrapper in card_wrappers:
                href = card_wrapper.find('a')['href']
                # Извлекаем последнее слово из введенного пользователем сайта
                last_word = url.split('/')[-1]
                # Проверяем, содержит ли ссылка последнее слово из введенного пользователем сайта
                if last_word in href:
                    # Записываем ссылку в файл
                    file.write(f'{href}\n')

        print("Ссылки успешно сохранены в файл card__wrapper.html")

    else:
        print(f"Ошибка подключения. Код статуса: {response.status_code}")

except Exception as e:
    print(f"Произошла ошибка: {e}")

# Разбираем базовый URL
parsed_url = urlparse(url)
# Формируем базовый URL без пути
base_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))

# Открываем файл card__wrapper.html для чтения
with open('Baza/card__wrapper.html', 'r', encoding='utf-8') as file:
    # Читаем все строки из файла
    lines = file.readlines()

# Открываем файл card__wrapper.html для перезаписи
with open('Baza/card__wrapper.html', 'w', encoding='utf-8') as file:
    # Проходимся по каждой строке и добавляем в начало базовый адрес
    for line in lines:
        # Убедимся, что строка не пуста перед добавлением
        if line.strip():
            # Добавляем базовый адрес в начало строки и записываем обратно в файл
            file.write(f'{base_url}{line}\n')

print("Ссылки успешно обновлены в файле card__wrapper.html")


# Открываем CSV-файл для записи
with open('Baza/baza.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Создаем объект для записи CSV
    csv_writer = csv.writer(csvfile)

    # Записываем дату формирования отчета
    csv_writer.writerow(['Дата формирования отчета:', datetime.now().strftime('%Y-%m-%d %H:%M:%S')])
    # Записываем заголовки
    csv_writer.writerow(['Группа товара:', 'Название товара:', 'Коллекция:', 'Розничная цена:', 'Размер (В*Ш*Г), мм:',
                        'Цвет каркасов:', 'Материал каркасов:', 'Цвет фасадов:', 'Материал фасадов:', 'Отделка фасадов:',
                        'Толщина кромки, мм:', 'Полезная информация:', 'Цвет столешницы:', 'Толщина столешницы, мм:',
                        'Масса брутто, кг:', 'Объем, куб.м:'])

    # Читаем данные из card__wrapper.html и записываем в CSV
    with open('Baza/card__wrapper.html', 'r', encoding='utf-8') as cardfile:
        lines = cardfile.readlines()
        for line in lines[2:]:  # Начинаем с третьей строки, так как первые две строки уже использованы
            # Заменяем '\n' в конце строки на пустую строку и разделяем данные по '|'
            data = line.strip().split('|')
            # Записываем данные в CSV
            csv_writer.writerow(data)

print("Данные успешно записаны в файл baza.csv")
