from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "com.abccompany.app",
    "appActivity": "com.abccompany.MainActivity",
    "automationName": "UiAutomator2",
    "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    # HR -> Check-IN
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "HR").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Check-IN")').click()
    time.sleep(1)
    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/checkin_btn").click()

    time.sleep(2)

    # Leave Application
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Leave Application")').click()
    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/leave_type").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Casual Leave")').click()

    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/from_date").click()
    # select date logic

    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/to_date").click()
    # select date logic

    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/leave_reason").send_keys("Feeling unwell")

    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/submit_leave").click()

    time.sleep(2)
    driver.save_screenshot("leave_confirmation.png")

finally:
    driver.quit()

