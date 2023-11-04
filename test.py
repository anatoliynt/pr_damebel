from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from urllib.parse import urlparse

# Указываете путь к драйверу
driver_path = 'e:\Soft\chromedriver_win32'

# Устанавливаем начальное время и максимальное время выполнения в секундах (например, 300 секунд)
start_time = time.time()
max_run_time = 15  # Время в секундах

# Создаем экземпляр драйвера
driver = webdriver.Chrome()
# Открываем веб-страницу
driver.get("https://hypermarketmebel.ru/catalog/tumby_dlya_obuvi/")

# Получаем имя папки согласно текущему адресу
page_url = driver.current_url
parsed_url = urlparse(page_url)
page_name = os.path.basename(parsed_url.path)

# Создаем директорию для сохранения HTML-файлов
save_directory = 'Z:/Training/Programmer/!Python/Project/pr_damebel/HTML'
page_directory = os.path.join(save_directory, page_name)

if not os.path.exists(page_directory):
    os.makedirs(page_directory)

# Прокручиваем страницу до конца
while True:
    # Выполняем скрипт JavaScript для прокрутки страницы
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Ждем некоторое время, чтобы динамические элементы загрузились
    time.sleep(2)

    # Проверяем, достигли ли мы конца страницы
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    scroll_position = driver.execute_script("return window.scrollY")
    if scroll_position >= scroll_height:
        break

    # Проверяем, если время выполнения превысило максимальное время
    current_time = time.time()
    if current_time - start_time > max_run_time:
        break

# Получаем и сохраняем HTML-код страницы
html_content = driver.page_source
page_name = page_name + ".html"
save_path = os.path.join(page_directory, page_name)
with open(save_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

# Закрываем браузер
driver.quit()
