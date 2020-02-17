import unittest
from selenium import webdriver
from  credential import login, password
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginMailBox(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_user_login(self):
        driver = self.driver
        driver.get("https://mail.ukr.net/desktop/login")
        driver.find_element_by_id("id-l").send_keys(login)
        driver.find_element_by_id("id-p").send_keys(password)
        driver.find_element_by_xpath("/html/body/div/div/main/form/button").click()
        user_mail = WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/ul/li[4]')))

        assert user_mail.text == login

    def tear_down(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

