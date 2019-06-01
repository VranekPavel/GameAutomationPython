class Village:

    driver = None

    def __init__(self, driver):
        Village.driver = driver

    def go_main(self):
        Village.driver.find_element_by_xpath("//div[contains(@class, \"visual-label-main\")]").click()

    def go_place(self):
        Village.driver.find_element_by_xpath("//div[contains(@class, \"visual-label-place\")]").click()

    def get_coordinates(self):
        return Village.driver.find_element_by_xpath("//tr[@id=\"menu_row2\"]/td[@class=\"box-item\"]/b").text[1:8]
