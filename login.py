from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Запускаем веб-драйвер (предполагается, что chromedriver.exe находится в папке проекта)
driver = webdriver.Chrome()

# Запрашиваем у пользователя адрес сайта
url = "https://mebel.com/"

try:
    # Открываем сайт в браузере
    driver.get(url)

    # Увеличиваем время ожидания до 20 секунд
    wholesale_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.icon.icon-sign-in[data-modal="modal_wholesale"]'))
    )

    # Нажимаем на кнопку "Войти в режим дилера"
    wholesale_button.click()

    # Добавляем паузу в 5 секунд
    time.sleep(5)

    # Ожидаем все поля ввода пароля
    password_inputs = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.NAME, 'password'))
    )

    # Проверяем, есть ли второе поле ввода пароля
    if len(password_inputs) >= 2:
        # Вводим пароль во второе поле (здесь используем "8021", вы можете заменить его на ваш пароль)
        password_inputs[1].send_keys("8021")
        print("Успешно введен пароль во второе поле")
    else:
        print("Второго поля ввода пароля не найдено")

    # Добавляем еще одну паузу в 2 секунды перед завершением
    time.sleep(2)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Не закрываем браузер автоматически
    # driver.quit()
    time.sleep(3)
# Находим кнопку "Войти"
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[7]/div[1]/div[2]/form/button'))
)

# Нажимаем на кнопку "Войти"
login_button.click()
print("Пользователь успешно вошел!")
# Добавляем паузу в 5 секунд для того, чтобы вы могли видеть результаты
time.sleep(5)
