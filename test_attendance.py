from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    "appPackage": "com.abccompany.app",  # Replace with real app package
    "appActivity": "com.abccompany.MainActivity",  # Replace with real activity
    "automationName": "UiAutomator2",
    "noReset": True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

try:
    # Login if needed here (skip if already logged in)
    
    # Navigate to HR -> My Attendance
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "HR").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("My Attendance")').click()

    # Set From and To Date
    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/from_date").click()
    # select date logic here (add later)

    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/to_date").click()
    # select date logic here (add later)

    # Filter Status = On Leave
    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/status_filter").click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("On Leave")').click()

    # Submit search
    driver.find_element(AppiumBy.ID, "com.abccompany.app:id/search_btn").click()
    time.sleep(3)

    # Screenshot
    driver.save_screenshot("attendance_result.png")

finally:
    driver.quit()
