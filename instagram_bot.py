from selenium import webdriver
import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://instagram.com')
        time.sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
        time.sleep(3)

    def search_for_posts(self, tag):
        self.driver.get(f'https://instagram.com/explore/tags/{tag}/')
        time.sleep(3)
        for i in range(1, 4):
            self.driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
        posts = self.driver.find_elements_by_tag_name('a')
        pattern = 'https://www.instagram.com/p/'
        url_list = []
        self.url_list = url_list
        for post in posts:
            link = post.get_attribute('href')

            if link.find(pattern) != -1:
                url_list.append(link)
            else:
                return

    def like_all_posts(self):
        for post in self.url_list:
            self.driver.get(post)
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div/div[3]/div/div/section[1]/span[1]/button').click()
            time.sleep(2)

        self.driver.close()


robot = InstaBot('yourusername', 'yourpassword')
robot.login()
robot.search_for_posts('explorepage')
robot.like_all_posts()
