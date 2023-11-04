from bs4 import BeautifulSoup
import os

html_code = input("ВВедите код: ")
# Создаем объект BeautifulSoup для разбора HTML
soup = BeautifulSoup(html_code, 'html.parser')

# Находим все теги <a> с классом "l-head-menu__link"
links = soup.find_all('a', class_='l-head-menu__link')

# Создаем пустой список для значений
values = []

# Извлекаем текст из найденных ссылок и добавляем их в список
for link in links:
    values.append(link.get_text())

# Указываем путь к директории, в которой нужно создать папки
base_path = r"C:\Users\a.grigorev\Documents\Задачи\Маг\Парсер\Карта сайта"

# Список значений из HTML (ваш список values)
values = ['Сад и дача', 'Кухня', 'Шкафы', 'Мягкая мебель', 'Гостиная', 'Прихожая', 'Спальня', 'Матрасы', 'Детская', 'Ванная', 'Для дома', 'Свет', 'Офис', 'Акции']

# Создаем папки согласно значениям
for value in values:
    folder_path = os.path.join(base_path, value)

    # Проверяем, существует ли папка, и создаем ее, если она не существует
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

print("Папки созданы успешно.")