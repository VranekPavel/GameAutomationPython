import unittest
import time
import random
from selenium import webdriver
from src.objects import login_page
from src.objects.village_page import Village
from src.objects.place_page import Place
from src.functions.file_methods import *
from src.functions.comparator import *
from selenium.webdriver.support.ui import WebDriverWait


class TestClass(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        login_page.login_function(driver, wait)

    def test_loot(self):
        driver = self.driver
        repeat = 0
        village = Village(driver)
        village.go_place()
        place = Place(driver)
        villages = read_file("loot.txt")
        villages.sort(key=lambda e: count_distance(e, village.get_coordinates()))
        #TODO implement repeat stop condition
        for target in villages:
            time.sleep(random.random() / 100)
            if not place.select_village(target[0: 8]):
                continue
            repeat = place.select_troops_and_attack(repeat)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()