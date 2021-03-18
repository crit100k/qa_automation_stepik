from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    sum1 = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)

    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_value(str(sum1))

    button = browser.find_element_by_tag_name(".btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # пустая строка