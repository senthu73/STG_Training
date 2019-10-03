import unittest

from selenium import webdriver
# from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Python\helloworld\Automation_Training\chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        #   self.driver.get("https://www.google.com")

        self.driver.get("https://www.copart.com/")
        print("Auto Auction - Copart USA - Salvage Cars For Sale", self.driver.title)
        self.assertIn("Auto Auction - Copart USA - Salvage Cars For Sale", self.driver.title)
        self.assertEqual("Auto Auction - Copart USA - Salvage Cars For Sale", self.driver.title)

        search = self.driver.find_element_by_id("input-search")

        search_entry = input("Enter Auto Model Name: ")
        print(search_entry)
        search.send_keys(search_entry + Keys.ENTER)
        search.send_keys(Keys.CONTROL, "a")

        search.send_keys(Keys.CLEAR)
        search.send_keys("toyota" + Keys.ENTER)

        table1 = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")
        a1 = table1.text
        print(a1)
        field1 = table1.get_attribute("innerHTML")
        print(field1)
        self.assertIn("TOYOTA", field1)
        print("test")

    def test1(self):
        self.assertEqual(4 + 5, 9)

    def test2(self):
        self.assertNotEqual(5 * 2, 13)

    def test3(self):
        self.assertTrue(4 + 5 == 9, "The result is False")

    def test4(self):
        self.assertTrue(4 + 5 == 9, "assertion fails")

    def test5(self):
        self.assertIn(3, [1, 2, 9])

    def test6(self):
        self.assertNotIn(3, range(3))


if __name__ == '__main__':
    unittest.main()
