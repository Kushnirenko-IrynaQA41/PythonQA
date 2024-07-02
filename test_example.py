import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        yield browser
        browser.close()

def test_playwright_example(browser):
    page = browser.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
    page.screenshot(path="example.png")

if __name__ == "__main__":
    pytest.main()
