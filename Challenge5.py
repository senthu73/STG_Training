import time
import unittest
import urllib.response

from selenium import webdriver
from Challenges_Main import STGChallenges

# from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC


class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        self.driver.get("https://www.copart.com/")
        print("Auto Auction - Copart USA - Salvage Cars For Sale", self.driver.title)
        modelsP = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        model_count = len(modelsP)
        print("********* For Loop data's from Popular Searches")
        for i in modelsP:
            print(i.text + " :: Link " + i.get_attribute("href"))
            print(" ********** End of FOR  loop data's *************************** ")

        search = self.driver.find_element_by_id("input-search")

        # search_entry = input("Enter Auto Model Name: ")
        search_entry = "porsche"
        print(search_entry)
        search.send_keys(search_entry + Keys.ENTER)
        time.sleep(4)
        # search.send_keys(Keys.CONTROL, "a")


        table1 = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")

        current_url = self.driver.current_url
        navigate_url = "https://www.copart.com/lotSearchResults/?free=true&query=" + search_entry
        print(current_url)
        print(navigate_url)

        if current_url == navigate_url:
            print("Match")
            # select drop down to choose value 100
            obj_element = Select(self.driver.find_element_by_name("serverSideDataTable_length"))
            obj_element.select_by_index(2)
            obj_element.select_by_value("100")
            obj_element.select_by_visible_text("100")
            time.sleep(3)

            model_objs = self.driver.find_elements(By.XPATH, '//span[@data-uname = "lotsearchLotmodel"]')
            print("-----------------------------------------------------------")
            print("Total " + search_entry + "in the page of 100 is : " + str(len(model_objs) - 1))
            print("-----------------------------------------------------------")
            obj_icon = self.driver.find_element(By.XPATH, '//*[@id="filters-collapse-1"]/div[1]/ul/li[4]/h4/a[1]/i')
            obj_icon.click()

            search_models = self.driver.find_element(By.XPATH, '//*[@id="collapseinside4"]/form/div/input')
            search_models.send_keys("CAYENNE S" + Keys.ENTER)
            time.sleep(2)


            # obj_Model = self.driver.find_elements(By.XPATH, '//*[@id="collapseinside4"]/ul/li//input')
            obj_Model = self.driver.find_elements(By.XPATH, '// span[ @ data - uname = "lotsearchLotmodel"]')

            print(obj_Model)
            print(len(obj_Model))
            for j in obj_Model:
                j.click()
                # print(j.text)
                print("----------------------------------------------------------")
                print("Total " + search_entry + " Make CAYENNE S is " + str())
                print("----------------------------------------------------------")
                damage_icon = self.driver.find_element(By.XPATH,
                                                       '//*[@id="filters-collapse-1"]/div[1]/ul/li[13]/h4/a[1]/i')

                # '//*[@data-uname ="DamageFilter"]/i')
                damage_icon.click()
                time.sleep(2)
                damage_search = self.driver.find_element(By.XPATH,
                                                         '//*[@id="collapseinside13"]/form/div/input')
                damage_search.send_keys("REAR END" + Keys.ENTER)

                for k in damage_search:
                    k.click()
                    time.sleep(2)
                    showing_no = self.driver.find_element(By.XPATH, '//*[@id="serverSideDataTable_info"]')
                    print(showing_no.text)

                    demage_models = self.driver.find_element(By.XPATH, '//*[@id="collapseinside4"]/form/div/input')
                    demage_models.send_keys("REAR END" + Keys.ENTER)

            # print(obj_element)
            # obj_element.select_by_value(100)
            # print(obj_element.select_by_value(100))
            # print(obj_element.select_by_index(1))

            # word = self.driver.find_elements(By.XPATH,  "//*[@id=\'serverSideDataTable_length\']/label/select/option")                  #"//*[@class =\"dataTables_info\"]")
            # print(word)
            # total = word.get_attribute("value")
            # print(total)


if __name__ == '__main__':
    unittest.main()
