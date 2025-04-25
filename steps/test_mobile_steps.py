from typing import Any

import allure
from behave import given
from behave import when, then

from common.mobile_auto import MobileAuto

mobile_auto = MobileAuto()


@allure.step("I have opened the MyObservatory app and finished initial settings")
@given("I have opened the MyObservatory app and finished initial settings")
def step_impl(context: Any) -> None:
    mobile_auto.disclaimer_page.agree_button.click()
    mobile_auto.privacy_policy_statement_page.agree_button.click()
    mobile_auto.system_elements.allow_notifications_button.click()
    mobile_auto.system_elements.background_access_to_location_ok_button.click()
    mobile_auto.system_elements.device_location_while_using_the_app_button.click()
    mobile_auto.system_elements.location_permission_back_button.click()
    mobile_auto.open_app_flyer_page.forward_button.click()
    mobile_auto.open_app_flyer_page.close_button.click()


@allure.step("I click side menu button")
@when("I click side menu button")
def step_impl(context: Any) -> None:
    mobile_auto.main_page.side_menu_button.click()


@allure.step("I expand Forecast & Warning Services")
@when("I expand Forecast & Warning Services")
def step_impl(context: Any) -> None:
    mobile_auto.main_page.side_menu_pane.forecast_and_warning_services_button.click()


@allure.step("I select 9-Day Forecast button")
@when("I select 9-Day Forecast button")
def step_impl(context: Any) -> None:
    mobile_auto.main_page.side_menu_pane.nine_day_forecast_button.click()


@allure.step("I should see the panel of 9-Day Forecast")
@then("I should see the panel of 9-Day Forecast")
def step_impl(context: Any) -> None:
    mobile_auto.nine_day_forecast_page.nine_day_forecast_header.assert_element_exist()


@allure.step("I should see the weather data of the 9th day")
@then("I should see the weather data of the 9th day")
def step_impl(context: Any) -> None:
    mobile_auto.nine_day_forecast_page.swipe_window_to_top()
    mobile_auto.nine_day_forecast_page.ninth_day_weather.assert_element_exist()
