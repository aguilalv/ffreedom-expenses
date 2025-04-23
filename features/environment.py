import os
from playwright.sync_api import sync_playwright


def before_all(context):
    # 1) Check if user provided a base_url via the -D option
    base_url = context.config.userdata.get("BASE_URL")
    # 2) If not provided, fall back to an environment variable
    #    or a default localhost
    if not base_url:
        base_url = os.getenv("BASE_URL", "http://127.0.0.1:5000")

    context.base_url = base_url
    print(f"[BEHAVE] Using BASE URL: {context.base_url}")

    # Start Playwright
    context.playwright = sync_playwright().start()

    # pick your engine based on userdata (see section #2)
    engine = context.config.userdata.get("browser", "chromium")
    headless = context.config.userdata.get("headless", "true").lower() == "true"

    context.browser = getattr(context.playwright, engine).launch(
        headless=headless, slow_mo=0  # or read from userdata
    )

    # context.browser = context.playwright.chromium.launch()


def before_scenario(context, scenario):
    # Create a new browser context for each scenario
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()


def after_scenario(context, scenario):
    # Close the page after each scenario
    context.page.close()
    context.browser_context.close()


def after_all(context):
    # Clean up Playwright
    context.browser.close()
    context.playwright.stop()
