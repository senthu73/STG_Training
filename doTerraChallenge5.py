import time
import unittest
import urllib.response

from selenium import webdriver


# from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC


class Challenge5_doTerra(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_doT_HW1_challenge5(self):
        self.driver.get("https://www.doterra.com/US/en/pl/single-oils")
        print("Single Oils - dōTERRA Product Line | dōTERRA Essential Oils", self.driver.title)
        obj_element = Select(self.driver.find_element_by_name("sort"))
        obj_element.select_by_visible_text("Popular")
        time.sleep(3)
        doTerra_image_urls = self.driver.find_elements(By.XPATH,
                                                       '//*[@id = "content_body"]//div/a[@class="prod-image"]')
        print("--------------------------------------------------------------------------------------------")
        print("Total Oil's on the Page : " + str(len(doTerra_image_urls))  + "Below is the list of 10 oils")
        print("--------------------------------------------------------------------------------------------")
        n = 1
        for i in doTerra_image_urls:
            print(str(n) + " :: Link " + i.get_attribute("href"))
            n += 1
            if n >= 11:
                break
                print("------------------------- End HW1 ---------------------------------------------------------------")

    def test_doT_HW2_challenge5(self):
        self.driver.get("https://www.doterra.com/US/en/pl/single-oils")
        doTerra_footer_urls = self.driver.find_elements(By.XPATH, '//*[@id="footer"]//a')
        print("--------------------------------------------------------------------------------------------")
        print("All the Footers links on this Page : " + str(len(doTerra_footer_urls)) )
        print("--------------------------------------------------------------------------------------------")
        m = 1
        for j in doTerra_footer_urls:
            print(str(m) + " :: Link " + j.get_attribute("href"))
        print("------------------------- End HW2 ---------------------------------------------------------------")


    def test_doT_HW3_challenge5(self):
        self.driver.get("https://www.doterra.com/US/en/product-education-blends")
        doTerra_label_urls = self.driver.find_elements(By.XPATH, '//*[@id="grid-view"]//span')
        print("--------------------------------------------------------------------------------------------")
        print("Count how many products name labeled Doterra : " + str(len(doTerra_label_urls)))
        print("--------------------------------------------------------------------------------------------")
        k = 1
        doTerra_label_count = 0
        for k in doTerra_label_urls:

            print( " ->:Product Label \t" + k.text)
            search_text = k.text.find("doTERRA")
            if search_text == 0:
                doTerra_label_count = doTerra_label_count + 1
        print("------------------------- End HW3 ---------------------------------------------------------------")
        print("Total doTERRA label products on the items " + str(doTerra_label_count))

if __name__ == '__main__':
    unittest.main()
