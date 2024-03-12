from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get("http://olx.uz")
browser.save_screenshot("screenshots/screen2.png")
time.sleep(15)
assert (
    "Доска объявлений OLX.uz, ранее Torg: сайт объявлений в Узбекистане - купля/продажа бу товаров на OLX.uz"
    in browser.title
)
print("olx.uz test success")



browser.get("https://tashkent.hh.uz/")
browser.save_screenshot("screenshots/screen3.png")
time.sleep(5)
assert (
    "Работа в Ташкенте, поиск персонала и публикация вакансий - tashkent.hh.uz"
    in browser.title
)
print("hh.uz test success")


