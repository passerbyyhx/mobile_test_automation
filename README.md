# mobile_test_automation

## 1. Installation

1.1 Install JDK >= 1.8  
https://www.oracle.com/hk/java/technologies/downloads/archive/  
Require add JDK path to system environment variable `"JAVA_HOME"`.

1.2 Python >= 3.10  
https://www.python.org/downloads/  
In the virtual environment of the project, use this command to add dependencies:  
`pip install -r requirements.txt`

1.3 Android Studio (Recommend Latest)  
https://developer.android.com/studio
Required modules:  
Android SDK (Recommend Android 15 or 16), and the corresponding path must be added to system environment variable
`"ANDROID_HOME"`. Also, the `common/config.ini` also require change to the current Android SDK path.  
Android SDK Build Tools  
Android SDK Command-line Tools (Latest)  
Android Emulator (After installation, require at least one Android Virtual Device added)  
Android SDK Platform Tools

1.4 Node.JS >= 16, npm >= 8  
https://nodejs.org/en/download

1.5 Appium Server (Recommend Latest)  
`npm install -g appium`

1.6 UiAutomator2
`appium driver install uiautomator2`
After installation, in the python virtual environment, use the following commands for initialize:  
`pip install --upgrade --pre uiautomator2`  
`python -m uiautomator2 init`

1.7 Appium Inspector  
https://github.com/appium/appium-inspector

1.8 allure  
`irm get.scoop.sh | iex`  
`scoop install allure`  
After installation, use `allure --version` for checking whether the installation is correct.  
Also, the installation path of allure (typically `C:\Users\<current user>\scoop\apps\allure\current`) needs to be added
in environment variable `ALLURE_HOME` and `PATH`.

## 2. Project infrastructure

mobile_test_automation&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Project root*    
│  
├─allure-results&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Storage of test results for report generation*  
│  
├────common&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Commonly used functions, mobile page instances and config files*  
│&ensp;&ensp;&ensp; │  
│&ensp;&ensp;&ensp; └──base_classes&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Base definitions of mobile page/pane/element. All actual definitions must inherit these classes*    
│  
├─features&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*BDD feature files*  
│  
├─mobile_elements&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Definitions of the mobile pages/panes/elements*    
│  
├─screenshots&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*Screenshots taken during the execution*    
│  
└─steps&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;*BDD step files*  

## 3. Steps for creating a new test
 - Create feature file and generate blank step definitions.
 - Manually run the test case, note down the page elements interacted.
 - Check whether the page/pane/element above is already created in `mobile_elements`, if not:
   - Create a new `<page name>_page.py` if the page does not exist;
   - Create definitions for the new element after the previous step, if the page exists yet element does not, create the element directly;
   - A pane definition is only required when a collection of elements are in the same region.
 - Using the defined elements, fill in the step definitions created before.  
  
## 4. Execution
 - Open a command line prompt and change directory to project root;
 - Use `behave` to run all features under `features` folder, or:
 - Use `behave ./features/<feature name>.feature` to run a specific feature;
 - After execution, use `allure serve` to view the html report.  

## 5. Demo test case design
In order to check the 9th day’s weather forecast from 9-day forecast screen, the following feature is designed:
  
`Given I have opened the MyObservatory app and finished initial settings`  
This step is to complete all the pre-testing steps, including but not limited to notification/location settings, close open flyer, etc. If a series of the test all need this step, this can be changed to a `before scenario/feature/all` hook for reducing code amount.
  
`When I click side menu button`  
`And I expand Forecast & Warning Services`  
`And I select 9-Day Forecast button`  
Steps prior to seeing the 9-day forecast page.  
  

`Then I should see the panel of 9-Day Forecast`  
At this page, the whole panel should be seen, hence the existence of the panel is checked.
  
`And I should see the weather data of the 9th day`  
The data grid of the 9th day should also be seen, hence the script will also check whether it exists.
  
  
