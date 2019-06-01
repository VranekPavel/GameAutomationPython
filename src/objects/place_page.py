from selenium.webdriver.common.keys import Keys


class Place:

    driver = None

    def __init__(self, driver):
        Place.driver = driver

    def select_village(self, village):
        place_target = Place.driver.find_element_by_xpath("//div[@id=\"place_target\"]/input")
        Place.driver.execute_script("arguments[0].value='" + village.strip() + "'", place_target)
        place_target.send_keys(Keys.ENTER)

    def select_troops_and_attack(self, repeat):
        target_distance = Place.driver.find_element_by_xpath("//div[@class=\"target-select-autocomplete\"]//span[@class=\"village-distance\"]")
        tempate_a = Place.driver.find_element_by_xpath("(//table/tbody/tr//a[@class=\"troop_template_selector\"])[1]")
        tempate_b = Place.driver.find_element_by_xpath("(//table/tbody/tr//a[@class=\"troop_template_selector\"])[2]")
        attack = Place.driver.find_element_by_id("target_attack")
        distance = int(float(target_distance.text[12: 14]))
        if distance <= 5 and repeat == 0:
            tempate_a.click()
            attack.click()
            try:
                Place.driver.find_element_by_id("troop_confirm_go").click()
            except:
                tempate_b.click()
                attack.click()
                try:
                    Place.driver.find_element_by_id("troop_confirm_go").click()
                    repeat = 1
                except:
                    pass
        else:
            tempate_b.click()
            attack.click()
            try:
                Place.driver.find_element_by_id("troop_confirm_go").click()
            except:
                repeat = 2
        return repeat