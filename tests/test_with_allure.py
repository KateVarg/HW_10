from selene import browser, by, be
import allure


def test_with_allure():
    with allure.step('Открытие сайта'):
        browser.open('')

    with allure.step('Нажатие на поле поиска'):
        browser.element('.search-input').click()

    with allure.step('Ввод и поиск репозитория'):
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Открытие репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Переход в Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверка отображения нужной Issues'):
        browser.element(by.partial_text('#88')).should(be.visible)
