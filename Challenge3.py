import unittest

from selenium import webdriver
# from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Python\helloworld\Automation_Training\chromedriver.exe")

    def tearDown(self):
        self.driver.close()



    def test_challenge3(self):
        self.driver.get("https://www.copart.com/")
        print("Auto Auction - Copart USA - Salvage Cars For Sale", self.driver.title)
        modelsP = self.driver.find_elements(By.XPATH, "//*[@ng-if=\"popularSearches\"]//a")
        model_count = len(modelsP)
        print("********* For Loop data's from Popular Searches")
        for i in modelsP:
            print(i.text + " :: Link " + i.get_attribute("href"))
            print(" ********** End of FOR  loop data's *************************** ")

    def test_challenge3_While(self):

        self.driver.get("https://www.copart.com/")
        cat = self.driver.find_element(By.XPATH, "//*[@ng-if = \"popularSearches\"]/../div[2]//h4")
        print(cat)

        categories = self.driver.find_elements(By.XPATH, "//*[@ng-if =\"popularSearches\"]/../div[3]//a")
        print(categories)
        print(categories[0])
        # categories_count = len(categories)
        i = 0
        print("----------- While LOOP ---------------")
        while i < len(categories):
            print(i)
            print(categories[i].text + " :: Link " + categories[i].get_attribute("href"))
            i += 1


        print("----------- End of WHILE loop --------------------------")



if __name__ == '__main__':
    unittest.main()
