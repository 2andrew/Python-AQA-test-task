import os
import re
import sys

import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config import settings

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.makedirs("screenshots", exist_ok=True)


@pytest.fixture(scope="function")
def init_driver(browser_config):
    browser = browser_config["browser"]
    run_mode = settings.RUN_MODE.lower()

    if run_mode == "local":
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--window-size=1920,1080")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = FirefoxOptions()
            options.binary_location = '/usr/bin/firefox'
            options.profile = FirefoxProfile()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
            driver = webdriver.Firefox(options=options)
        else:
            raise ValueError(f"Unsupported local browser: {browser}")
    elif run_mode == "selenoid":
        capabilities = {
            "browserName": browser
        }
        if browser == "chrome":
            options = ChromeOptions()
            options.add_argument("--window-size=1920,1080")
        elif browser == "firefox":
            options = FirefoxOptions()
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        for key, value in capabilities.items():
            options.set_capability(key, value)

        _test_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]
        _test_name = re.sub(r'[^\w.-]', '_', _test_name)

        selenoid_options = {
            "enableVideo": True,
            "enableVNC": True,
            "videoName": f"{_test_name}.mp4",
            "name": _test_name
        }
        options.set_capability("selenoid:options", selenoid_options)

        driver = webdriver.Remote(
            command_executor=settings.SELENOID_URL,
            options=options
        )
    else:
        raise ValueError(f"Unsupported RUN_MODE: {run_mode}")

    yield driver


def pytest_generate_tests(metafunc):
    SUPPORTED_BROWSERS = ["chrome", "firefox"]
    if "browser_config" in metafunc.fixturenames:
        marker = metafunc.definition.get_closest_marker("browsers")
        if marker:
            browsers = [b.strip().lower() for b in marker.args[0].split(",")]
        else:
            browsers = SUPPORTED_BROWSERS

        invalid = [b for b in browsers if b not in SUPPORTED_BROWSERS]
        if invalid:
            raise ValueError(f"Unsupported browsers in marker: {invalid}")

        browser_configs = [{"browser": b} for b in browsers]
        ids = [f"{config['browser']}" for config in browser_configs]
        metafunc.parametrize("browser_config", browser_configs, ids=ids, scope="function")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("init_driver", None)
        if driver:
            try:
                file_name = f"screenshots/{item.name}.png"
                driver.save_screenshot(file_name)
                print(f"\nScreenshot saved to: {file_name}")
            except Exception as e:
                print(f"\nFailed to take screenshot: {str(e)}")
