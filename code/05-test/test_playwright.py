from shiny.playwright import controller
from shiny.run import ShinyAppProc
from playwright.sync_api import Page
from shiny.pytest import create_app_fixture

app = create_app_fixture("app.py")


def test_basic_app(page: Page, app: ShinyAppProc):
    page.goto(app.url)

    select = controller.InputSelect(page, "species")
    select.expect_choices([
        "Adelie",
        "Gentoo",
        "Chinstrap",
    ])
    select.set("Adelie")
    select.expect_selected("Adelie")
