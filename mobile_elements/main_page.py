from common.base_classes.base_mobile_classes import BaseAndroidPage, BaseAndroidPane


class MainPage(BaseAndroidPage):
    def __init__(self, driver=None):
        BaseAndroidPage.__init__(self, driver=driver)

        # ============================================= Panes =============================================
        self.side_menu_pane = SideMenuPane(driver=self.driver)

        # ========================================= Page Elements =========================================
        self.side_menu_button = self.page.sub_element(
            "//android.widget.ImageButton[@content-desc='Navigate up']", name="Side menu button")


class SideMenuPane(BaseAndroidPane):
    def __init__(self, pane_locator="//android.widget.FrameLayout[@resource-id='hko.MyObservatory_v1_0:id/container']",
                 driver=None):
        BaseAndroidPane.__init__(self, pane_locator=pane_locator, driver=driver)

        self.forecast_and_warning_services_button = self.pane.sub_element(
            "//android.widget.TextView[@resource-id='hko.MyObservatory_v1_0:id/title' and @text='Forecast & Warning Services']",
            name="Forecast & Warning Services button")
        self.nine_day_forecast_button = self.pane.sub_element(
            "//android.widget.TextView[@resource-id='hko.MyObservatory_v1_0:id/title' and @text='9-Day Forecast']",
            name="9 Day Forecast button")
