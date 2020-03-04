from selenium import webdriver
import unittest

comm_page = 'https://github.com/django/django/commits/master'
main_page = 'https://github.com/django/django'
commit_value_path = '//clipboard-copy'
element_repo_path = '//*[@class="no-wrap d-flex flex-self-start flex-items-baseline"]/a'


class TestLastCommit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)

    def test_get_commit_id(self):
        """Finding and assertion Ids"""

        '''Getting id at commit page'''

        self.driver.get(comm_page)
        id_comm_page = self.driver.find_element_by_xpath(commit_value_path).get_attribute('value')
        print('comm page: {}'.format(id_comm_page))

        '''Getting id commit in the header of main page'''

        self.driver.get(main_page)
        link_repo = self.driver.find_element_by_xpath(element_repo_path).get_attribute('href').split('/')
        id_main_page = link_repo[-1]
        print('main page: {}'.format(id_main_page))

        '''Assertion commit ids from different pages'''

        self.assertEqual(id_main_page, id_comm_page, "id_main_page should be equal to id_comm_page")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
