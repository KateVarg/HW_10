from allure_commons.types import Severity
import allure
from modules.check_repo import open_page, click_search, type_name_for_search, open_repo, open_issues, check_issues


def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("Проверка наличия задачи #88")
    allure.dynamic.link("https://github.com", name="Ссылка на Github")
    open_page()
    click_search()
    type_name_for_search()
    open_repo()
    open_issues()
    check_issues()