from common.base_classes.base_mobile_classes import BaseAndroidPage


class SystemPage(BaseAndroidPage):
    def __init__(self, driver=None):
        BaseAndroidPage.__init__(self, driver=driver)

        # ========================================= Page Elements =========================================
        self.allow_notifications_button = self.page.sub_element(
            "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']",
            name="Allow Notifications button")
        self.dont_allow_notifications_button = self.page.sub_element(
            "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']",
            name="Don't Allow Notifications button")
        self.background_access_to_location_ok_button = self.page.sub_element(
            "//android.widget.Button[@resource-id='android:id/button1']", name="Back to Location OK button")
        self.device_location_precise_button = self.page.sub_element(
            "//android.widget.RadioButton[@resource-id='com.android.permissioncontroller:id/permission_location_accuracy_radio_fine']",
            name="Device Location - Precise button")
        self.device_location_approximate_button = self.page.sub_element(
            "//android.widget.RadioButton[@resource-id='com.android.permissioncontroller:id/permission_location_accuracy_radio_coarse']",
            name="Device Location - Approximate button")
        self.device_location_while_using_the_app_button = self.page.sub_element(
            "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']",
            name="Device Location - While the Using The App button")
        self.device_location_only_this_time_button = self.page.sub_element(
            "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_one_time_button']",
            name="Device Location - Only this time button")
        self.device_location_dont_allow_button = self.page.sub_element(
            "//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_deny_button']",
            name="Device Location - Don't Allow Button")
        self.location_permission_back_button = self.page.sub_element(
            "//android.widget.ImageButton[@content-desc='Navigate up']",
            name="Location Permission Back button")
