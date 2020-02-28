from datetime import datetime
from selenium import webdriver
import unittest

comm_page = 'https://github.com/django/django/commits/master'
main_page = 'https://github.com/django/django'

# comm_page = 'https://github.com/SeleniumHQ/selenium/commits/master'
# main_page = 'https://github.com/SeleniumHQ/selenium'

# comm_page = 'https://github.com/jenkinsci/jenkins/commits/master'
# main_page = 'https://github.com/jenkinsci/jenkins'


class TestLastCommit(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def test_get_commit_id(self):
        """Finding and assertion Ids"""

        '''Getting id at commit page'''

        self.driver.get(comm_page)
        last_comm = self.driver.find_elements_by_xpath(
            '//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/ol[*]/li[*]/div[2]/div/clipboard-copy')
        value_list = []
        for val in last_comm:
            commit_value = val.get_attribute('value')
            value_list.append(commit_value)

        '''Getting commit time'''

        last_com_time = self.driver.find_elements_by_xpath(
            '//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/ol[*]/li/div[*]/div/div[*]/relative-time')
        time_list = []
        for i in last_com_time:
            dt = i.get_attribute('datetime')
            commit_time = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%SZ')
            time_list.append(commit_time)

        '''Creating a dictionary id/time'''

        dict_id_time = dict(zip(value_list, time_list))
        for k, v in dict_id_time.items():
            print(k, v)
        print('-' * 60)

        '''Finding max value in dict'''

        max_value = max(dict_id_time.values())
        final_dict = {k: v for k, v in dict_id_time.items() if v == max_value}
        id_comm_page = list(final_dict)[0]
        print('comm page: {}'.format(id_comm_page))

        '''Getting id commit in the header of main page'''

        self.driver.get(main_page)
        element_repo = self.driver.find_element_by_xpath(
            '//*[@id="js-repo-pjax-container"]/div[2]/div/div[6]/div/div/div[3]/a')
        link_repo = element_repo.get_attribute('href').split('/')
        id_main_page = link_repo[-1]
        print('main page: {}'.format(id_main_page))

        '''Assertion commit ids from different pages'''

        assert id_main_page == id_comm_page

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
