import unittest
import time
import random
from selenium import webdriver
from src.objects.place_page import *
from src.objects.login_page import login_function
from src.objects.village_page import Village
from src.functions.file_methods import *
from src.functions.comparator import *
from selenium.webdriver.support.ui import WebDriverWait


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        login_function(driver, wait)

    def test_search_in_python_org(self):
        driver = self.driver
        repeat = 0
        village = Village(driver)
        village.go_place()
        place = Place(driver)
        villages = read_file("loot.txt")
        villages.sort(key=lambda e: count_distance(e, village.get_coordinates()))
        for target in villages:
            time.sleep(random.random() / 100)
            if not place.select_village(target[0: 8]):
                continue
            repeat = place.select_troops_and_attack(repeat)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()