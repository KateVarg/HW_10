from selene import browser, by, be
import allure


@allure.step('Открытие сайта')
def open_page():
    browser.open("https://github.com")


@allure.step('Нажатие на поле поиска')
def click_search():
    browser.element('.search-input').click()


@allure.step('Ввод и поиск репозитория')
def type_name_for_search():
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()


@allure.step('Открытие репозитория')
def open_repo():
    browser.element(by.link_text('eroshenkoam/allure-example')).click()


@allure.step('Переход в Issues')
def open_issues():
    browser.element('#issues-tab').click()


@allure.step('Проверка отображения нужной Issues')
def check_issues():
    browser.element(by.partial_text('#88')).should(be.visible)
