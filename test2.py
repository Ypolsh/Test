from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://example.com")

        assert "Example" in page.title()

        link = page.get_by_text("More information")
        link.click()

        assert page.url == "https://www.iana.org/help/example-domains"

        browser.close()

if __name__ == "__main__":
    test_example()
