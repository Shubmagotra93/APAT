import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from tests.base import Base


@pytest.fixture()
def setup(request):
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service("/home/shubham/PycharmProjects/APAT/chromedriver")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(10)
    # driver.get("https://www.amazon.in/")
    driver.get(Base.config_data()['url'])
    driver.maximize_window()

    request.cls.driver = driver  # this line will add driver reference in other classes

    before_failed = request.session.testsfailed
    yield driver
    if request.session.testsfailed != before_failed:
        allure.attach(driver.get_screenshot_as_png(), name=request.node.name, attachment_type=AttachmentType.PNG)
        request.session.testsfailed = before_failed  # Reset the testsfailed count
    driver.close()