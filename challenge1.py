
import unittest
from selenium import webdriver




class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\Python\helloworld\Automation_Training\chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge1_google(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)
        print("google")

    def test_challenge1_doterra(self):
        self.driver.get("https://www.doterra.com")
        self.assertIn("Essential Oils Pure and Natural | dōTERRA Essential Oils", self.driver.title)
        self.assertEqual("Essential Oils Pure", self.driver.current_url )
        print("doterra")

    def test_challenge1_yahoo(self):
        print("Chalenge 1")
        sValue = "Assert Equals Test";

        assertEquals("Assert Equals Test", sValue);

        print("Test Passed");

        self.driver.get("https://www.yahoo.com")
        self.assertIn("yahoo", self.driver.title)
        print("yahoo")

        flag = input("enter the flag(y/n):")
        assert flag =="y" or flag =="n", "Invalid flag, must be 'y' or 'n'"

if __name__ == '__main__':
         unittest.main()