from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = r"C:\Users\Junling\bin\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Go to target website and wait for load
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)

# Get relevant elements: cookie, count, and upgrade buttons
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

# Define main clicking action
actions = ActionChains(driver)
actions.click(cookie)

# Click 100 times while updating count
for i in range(100):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])

    # Check if upgrade is possible at current count. If yes, click on upgrade 
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()

driver.quit()