import os
from datetime import datetime
from time import sleep

import allure
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from common.base_classes import base_assert
from common.mobile_project_path import MobileProjectPath
from common.tool import Tool


class BaseAndroidElement:
    def __init__(self, element_locator="", driver: webdriver.webdriver.WebDriver = None, name=""):
        self.element_locator = element_locator
        self.driver = driver
        self.name = name
        self._element = None
        self.base_assert = base_assert.BaseAssert()
        self.tool = Tool()
        self.mobile_project_path = MobileProjectPath()

    @property
    def element(self):
        if self._element is None:
            self._element = self.wait_for_element(self.element_locator, require_default_wait=False, timeout=100)
        return self._element

    def wait_for_element(self, by=AppiumBy.XPATH, require_default_wait=False, default_wait_time=0,
                         timeout=15):
        element = None
        if require_default_wait or default_wait_time != 0:
            if default_wait_time == 0:
                default_wait_time = timeout
            sleep(default_wait_time)
        for i in range(timeout):
            try:
                element = self.driver.find_element(by=by, value=self.element_locator)
                if self._element is None:
                    self._element = element
            except:
                pass
            if element is None:
                sleep(0.5)
            else:
                break
        return element

    def sub_element(self, sub_element_locator, name=""):
        locator = self.element_locator + sub_element_locator
        sub_element = BaseAndroidElement(locator, self.driver, name)
        return sub_element

    def sub_element_with_index(self, sub_element_locator: str, index: any = 1):
        if index is None:
            locator = self.element_locator + sub_element_locator
        elif index > 0:
            locator = f"({self.element_locator}{sub_element_locator})[{index}]"
        elif index == -1:
            locator = f"({self.element_locator}{sub_element_locator})[last()]"
        elif index < -1:
            locator = f"({sub_element_locator}{sub_element_locator})[last(){index + 1}]"
        else:
            raise ValueError(f"Invalid index {index}")
        sub_element = BaseAndroidElement(locator, self.driver)
        return sub_element

    def get_and_save_screenshot(self):
        now = datetime.now()
        now_str = now.strftime("%Y_%m_%d_%H_%M_%S")
        screenshot_name = f"screenshot_{now_str}.png"
        save_path = os.path.join(self.mobile_project_path.screenshots_path, screenshot_name)
        self.driver.save_screenshot(save_path)
        return (save_path, screenshot_name)

    def is_element_exist(self, require_default_wait=False, default_wait_time=0,
                         timeout=15, poll_frequency=0.1):
        element_exists = False
        try:
            element = self.wait_for_element(require_default_wait=require_default_wait,
                                            default_wait_time=default_wait_time, timeout=timeout)
            if element is not None:
                element_exists = True
        except:
            element_exists = False
        return element_exists

    def assert_element_exist(self):
        element_exists = self.is_element_exist()
        self.base_assert.is_true(element_exists)

    def click(self, require_default_wait=False, timeout=15):
        with allure.step(f"{self.tool.get_current_datetime()} Clicking {self.name}"):
            element_exists = self.is_element_exist(require_default_wait=require_default_wait, timeout=timeout)
            if element_exists:
                save_path, screenshot_name = self.get_and_save_screenshot()
                self._element.click()
                allure.attach.file(save_path, screenshot_name, allure.attachment_type.PNG, extension="png")

    def input(self, content):
        with allure.step(f"{self.tool.get_current_datetime()} Typing {content} in {self.name}"):
            if self.is_element_exist():
                self._element.send_keys(content)

    def get_attribute(self, attribute):
        value = ""
        if self.is_element_exist():
            value = self._element.get_attribute(attribute)
        return value

    def get_element_text(self):
        current_text = ""
        if self.is_element_exist():
            try:
                current_text = self._element.text
            except:
                try:
                    current_text = self.get_attribute("text")
                except:
                    current_text = ""
        return current_text


class BaseAndroidPane:
    def __init__(self, pane_locator="", driver: webdriver.webdriver.WebDriver = None):
        self.pane_locator = pane_locator
        self.driver = driver
        self._pane = BaseAndroidElement(pane_locator, driver)

    @property
    def pane(self):
        return self._pane


class BaseAndroidPage:
    def __init__(self, page_locator="/hierarchy/android.widget.FrameLayout",
                 driver: webdriver.webdriver.WebDriver = None):
        self.page_locator = page_locator
        self.driver = driver
        self._page = BaseAndroidElement(page_locator, driver)

    @property
    def page(self):
        return self._page
