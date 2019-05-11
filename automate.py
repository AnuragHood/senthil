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
        self.driver.get("https://flipboard.com/")
    def test_flipboard(self):
        try:
            print("website title:", self.driver.title)
            images = self.driver.find_element_by_xpath("//*[@id='content']/div/main/div/ul/li[1]/article/div/a/div/img")
            options = self.driver.find_element_by_xpath("//*[@id='content']/div/main/div/div[1]/nav/ul")
            items = options.find_elements_by_tag_name("li")
            for item in items:
                text = item.text
                print("nav options available::",text)

            print("image urls",images.get_attribute("src"))

            like = self.driver.find_elements_by_css_selector('#content > div > main > div > ul > li:nth-child(5) > article > div > a > div')
            for x in range(0, len(like)):
                if like[x].is_displayed():
                    print(like[x].text)
                    photo = like[x].find_elements_by_tag_name("img")
                    for y in range(0, len(photo)):
                        print(photo[y].text)


        except Exception :
            print("Something went wrong in flipboard automation:")
            traceback.print_exc()
    def tearDown(self):
        # close the browser window
        self.driver.quit()



if __name__ == '__main__':
        unittest.main()