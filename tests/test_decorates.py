from modules.check_repo import open_page, click_search, type_name_for_search, open_repo, open_issues, check_issues


def test_decorates_step():
    open_page()
    click_search()
    type_name_for_search()
    open_repo()
    open_issues()
    check_issues()
