from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login_function(driver, wait):
    driver.get("https://www.divokekmeny.cz/")
    driver.find_element_by_id("user").send_keys("caymon")
    driver.find_element_by_id("password").send_keys("1241995")
    if driver.find_element_by_id("remember-me").get_attribute("checked") == "checked":
        driver.find_element_by_id("remember-me").click()
    driver.find_element_by_xpath("//a[@class=\"btn-login\"]").click()
    world = wait.until(EC.element_to_be_clickable((By.XPATH, "// a[@class = \"world-select\"]/span")))
    world.click()