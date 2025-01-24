from selenium import webdriver
import os
import allure
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to run tests on"
    )
    parser.addoption("--hub_url", help="URL of the Selenium Grid Hub")
    parser.addoption("--node_url", action="store", default=None, help="Node URL for Selenium Grid")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def setup(browser, request ):
    global driver
    browser_name = request.config.getoption("--browser").lower()
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options)
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options)
    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options)
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()


def pytest_html_report_title(report):
    report.title = "Test Result Report"

# Add screenshot on failed testcases
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        filepath = os.getcwd()
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = file_name.replace("/", "_")
            file_path = f"{filepath}\Screenshots\\{file_name}"
            _capture_screenshot(file_path)
            if file_name:
                html = '<div> <img src="%s"' \
                       ' alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_path
                extra.append(pytest_html.extras.html(html))
                allure.attach.file(file_path, name="Screenshot on Failure",
                                   attachment_type=allure.attachment_type.PNG)

                # driver.quit()
        report.extra = extra

#  capture screenshot
def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

# python -m pytest -m testmarker -s -v --capture=sys --html=Reports\finalreport.html --self-contained-html testCases/test_filename.py