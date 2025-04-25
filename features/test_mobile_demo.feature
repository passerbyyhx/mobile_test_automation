@test_hooks_tag
@allure.label.epic:TestMobileDemo
Feature: Test Mobile Demo

  @allure.label.story:Demo
  Scenario: Demo
    Given I have opened the MyObservatory app and finished initial settings
    When I click side menu button
    And I expand Forecast & Warning Services
    And I select 9-Day Forecast button
    Then I should see the panel of 9-Day Forecast
    And I should see the weather data of the 9th day