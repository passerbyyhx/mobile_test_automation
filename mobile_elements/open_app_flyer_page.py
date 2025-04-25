from common.base_classes.base_mobile_classes import BaseAndroidPage


class OpenAppFlyerPage(BaseAndroidPage):
    def __init__(self, driver=None):
        BaseAndroidPage.__init__(self, driver=driver)

        # ========================================= Page Elements =========================================
        self.forward_button = self.page.sub_element("//android.widget.ImageView[@content-desc='Next page']", name="Forward button")
        self.close_button = self.page.sub_element("//android.widget.ImageView[@content-desc='Close']", name="Close button")
