from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located



with webdriver.Firefox() as driver:

    wait = WebDriverWait(driver, 10)
    driver.get("http://google.com/ncr")
    driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)

    wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>a")))

    results = driver.find_elements_by_css_selector("h3>a")
    for i, result in results.iteritems():
        print(f"#{i}: {result.text} ({result.get_property('href')})")