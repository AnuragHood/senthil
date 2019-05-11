import traceback

from selenium import webdriver
import unittest
import sys



class flipboard(unittest.TestCase):
    """Search without any criteria test case"""

    # create a new browser  session

    def setUp(self):

        driver_required = input("Press 1 for firefox 2 for chrome 3 for safari for login test")
        if driver_required == "2":
            self.driver = webdriver.Chrome()
        elif driver_required == "1":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the procat home page
        self.driver.get("https://twitter.com/")
    def test_twitter(self):
        try:
            print("website title:", self.driver.title)
            self.driver.find_element_by_link_text("Log in").click()
            self.driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[1]/input").send_keys("sn.anurag.pathak@gmail.com")
            self.driver.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/fieldset/div[2]/input").send_keys("P@ssion@02")
            self.driver.find_element_by_class_name("EdgeButtom--medium").click();
            twitts = self.driver.find_element_by_xpath("//*[@id='stream-item-tweet-1127186719420420096']/div[1]/div[2]/div[2]/p")
            print("nav options available::",twitts.text)



        except Exception :
            print("Something went wrong in twitter automation:")
            traceback.print_exc()
    def tearDown(self):
        # close the browser window
        self.driver.quit()



if __name__ == '__main__':
        unittest.main()