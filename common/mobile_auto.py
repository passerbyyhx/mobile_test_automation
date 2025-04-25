import configparser
import os.path
import subprocess
from time import sleep

from appium import webdriver
from appium.options.android import UiAutomator2Options

from mobile_elements import system_elements, disclaimer_page, privacy_policy_statements_page, open_app_flyer_page, \
    main_page, nine_day_forecast_page


def wait_for_emulator_booting(timeout=15):
    sleep(5)
    for i in range(timeout):
        current_status = subprocess.Popen(f"adb devices -l", shell=True, stderr=subprocess.PIPE,
                                          stdout=subprocess.PIPE).stdout.read().decode('utf-8').split("          ")[1]
        if "offline" in current_status:
            sleep(1)
        else:
            sleep(15)
            break


def get_emulator_path_and_virtual_device_name():
    config = configparser.ConfigParser()
    config.read("common/config.ini")
    android_sdk_path = config.get("mobile_test", "android_sdk_path")
    emulator_path = os.path.join(android_sdk_path, "emulator", "emulator.exe")
    virtual_device_name = subprocess.Popen(f"{emulator_path} -list-avds", shell=True, stderr=subprocess.PIPE,
                                           stdout=subprocess.PIPE).stdout.read().decode('utf-8').replace("\r\n", "")
    return (emulator_path, virtual_device_name)

def start_virtual_device():
    emulator_path, virtual_device_name = get_emulator_path_and_virtual_device_name()
    subprocess.Popen(f"{emulator_path} -avd {virtual_device_name}", shell=True, stderr=subprocess.PIPE,
                     stdout=subprocess.PIPE)
    wait_for_emulator_booting()
    subprocess.Popen("appium", shell=True)


class MobileAuto:
    start_virtual_device()
    appium_server_url = "http://127.0.0.1:4723"
    virtual_device_name = get_emulator_path_and_virtual_device_name()[1]
    capabilities = dict(
        platformName="Android",
        automationName="uiautomator2",
        deviceName=virtual_device_name,
        appPackage="hko.MyObservatory_v1_0",
        newCommandTimeout="2000"
    )
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def __init__(self):
        self.system_elements = system_elements.SystemPage(driver=self.driver)
        self.disclaimer_page = disclaimer_page.DisclaimerPage(driver=self.driver)
        self.privacy_policy_statement_page = privacy_policy_statements_page.PrivacyPolicyStatementsPage(
            driver=self.driver)
        self.open_app_flyer_page = open_app_flyer_page.OpenAppFlyerPage(driver=self.driver)
        self.main_page = main_page.MainPage(driver=self.driver)
        self.nine_day_forecast_page = nine_day_forecast_page.NineDayForecastPage(driver=self.driver)
