from common.base_classes.base_mobile_classes import BaseAndroidPage


class DisclaimerPage(BaseAndroidPage):
    def __init__(self, driver=None):
        BaseAndroidPage.__init__(self, driver=driver)

        # ========================================= Page Elements =========================================
        self.agree_button = self.page.sub_element(
            "//android.widget.Button[@resource-id='hko.MyObservatory_v1_0:id/btn_agree']", name="Agree button")
        self.disagree_button = self.page.sub_element(
            "//android.widget.Button[@resource-id='hko.MyObservatory_v1_0:id/btn_not_agree']", name="Disagree button")
