from selenium import webdriver
import time

chrome_driver = "*******************"  # location of the chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get("http://orteil.dashnet.org/experiments/cookie/")  # gets the website to visit

# Get cookie to click on
cookie = driver.find_element_by_id("cookie")

# Get upgrade options ids
options = driver.find_elements_by_css_selector("#store div")
options_id = [option.get_attribute("id") for option in options]


timeout = time.time() + 5  # current time plus five seconds
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()  # clicks on cookie

    # Every 5 seconds
    if time.time() > timeout:

        # Get all the upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into integer
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))  # ensures the prices are formatted
                item_prices.append(cost)

        # Create a dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = options_id[n]  # left = key, right= value

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text  # gets the text
        if "," in money_element:
            money_element = money_element.replace(",", "")  # replace comma with space
        cookie_count = int(money_element)  # converts string into integer

        # Find upgrades we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        id_purchase = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(id_purchase).click()  # click on the most expensive affordable item

        # Add another five seconds until the next check
        timeout = time.time() + 5

    # After five minutes stop the bot and check the rate of cookies per second
    if time.time() > five_min:
        cookie_per_sec = driver.find_element_by_id("cps").text
        print(cookie_per_sec)
        break
