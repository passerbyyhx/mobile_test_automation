from datetime import datetime, timedelta

from common.base_classes.base_mobile_classes import BaseAndroidPage


class NineDayForecastPage(BaseAndroidPage):
    def __init__(self, driver=None):
        BaseAndroidPage.__init__(self, driver=driver)

        # ========================================= Page Elements =========================================
        self.nine_day_forecast_header = self.page.sub_element(
            "//android.widget.LinearLayout[@content-desc='9-Day Forecast']")
        time_now = datetime.now()
        today_string = time_now.strftime("%d %b")
        time_9_days_later = time_now + timedelta(days=9)
        time_9_days_later_string = time_9_days_later.strftime("%d %b")
        self.today_weather = self.page.sub_element(
            f"//android.widget.TextView[@content-desc='{today_string}']", name="Today Weather")
        self.ninth_day_weather = self.page.sub_element(
            f"//android.widget.TextView[@content-desc='{time_9_days_later_string}']", name="9th Day Weather")

    def swipe_window_to_top(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(start_x=width / 2, start_y=4 * height / 5, end_x=width / 2, end_y=0)
