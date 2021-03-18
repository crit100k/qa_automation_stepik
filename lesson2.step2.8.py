from selenium import webdriver
import time
import os


with open("file.txt", "w") as file:
    content = file.write("automationbypython")

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option1 = browser.find_element_by_name("firstname").send_keys("Alex")
    option2 = browser.find_element_by_name("lastname").send_keys("Test")
    option2 = browser.find_element_by_name("email").send_keys("test@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    browser.find_element_by_id("file").send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()