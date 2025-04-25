import allure
import requests.models


class BaseAssert:
    @staticmethod
    def are_equal(current_value: object, baseline: object) -> None:
        with allure.step(f"Assert whether current value {current_value} equals to baseline {baseline}:"):
            if type(current_value) != type(baseline):
                type_of_baseline = type(current_value)
                type_of_current_value = type(current_value)
                raise AssertionError(
                    f"Type of current value {type_of_current_value} is not equal to type of baseline {type_of_baseline}.")
            assert current_value == baseline, f"Current value {current_value} does not equal to {baseline}."

    def is_true(self, current_value: bool) -> None:
        with allure.step(f"Assert whether current value {current_value} is True:"):
            if type(current_value) is not bool:
                type_of_current_value = type(current_value)
                raise AssertionError(
                    f"Current value {current_value} is a {type_of_current_value}, not a boolean variable.")
            else:
                self.are_equal(current_value, True)

    def is_false(self, current_value: bool) -> None:
        with allure.step(f"Assert whether current value {current_value} is True:"):
            if type(current_value) is not bool:
                type_of_current_value = type(current_value)
                raise AssertionError(
                    f"Current value {current_value} is a {type_of_current_value}, not a boolean variable.")
            else:
                self.are_equal(current_value, False)

    @staticmethod
    def is_connected(response: requests.models.Response) -> None:
        with allure.step(f"Assert whether the connection was successful:"):
            if type(response) is not requests.models.Response:
                response_type = type(response)
                raise AssertionError(f"Invalid response type {response_type}.")
            else:
                status_code = str(response.status_code)
                assert status_code == "200", f"Connection failed. Current status code is {status_code}."

