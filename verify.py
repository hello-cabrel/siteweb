from playwright.sync_api import sync_playwright
import os

def run_cuj(page):
    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(1000)

    # Take a screenshot of the initial desktop view
    page.screenshot(path="/home/jules/verification/screenshots/verification.png")
    page.wait_for_timeout(500)

    # Scroll down to trigger the sticky header
    page.evaluate("window.scrollBy(0, 500)")
    page.wait_for_timeout(1000)

    # Switch to mobile view to test the hamburger menu
    page.set_viewport_size({"width": 375, "height": 812})
    page.wait_for_timeout(1000)

    # Click hamburger menu
    page.locator("#hamburger-menu").click()
    page.wait_for_timeout(1000)

    # Close menu by clicking a link
    page.locator("#mobile-menu .mobile-link").first.click()
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    os.makedirs("/home/jules/verification/videos", exist_ok=True)
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()
