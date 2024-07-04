from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

class InstaBot:
    def __init__(self, username, password, tag, iter):
        self.username = username
        self.password = password
        self.tag = tag
        self.iter = iter
        self.driver = webdriver.Chrome()

    def scroll_window(self, i):
        for x in range(1, i):
            self.driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)'
            )
            time.sleep(2)

    def login(self):
        self.driver.get('https://instagram.com')
        time.sleep(2)
        self.driver.find_element(By.NAME, 'username').send_keys(self.username)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.RETURN)
        time.sleep(8)

    def search_for_posts(self):
        self.driver.get(f'https://instagram.com/explore/tags/{self.tag}/')
        time.sleep(3)
        self.scroll_window(self.iter)
        posts = self.driver.find_elements(By.TAG_NAME, 'a')
        url_list = []
        for post in posts:
            link = post.get_attribute('href')
            if link.find('/p/') != -1:
                url_list.append(link)
        return url_list
    

    def like_all_posts(self):
        self.login()
        url_list = self.search_for_posts()
        for url in url_list:
            self.driver.get(url)
            time.sleep(2)
            icons = self.driver.find_elements(By.TAG_NAME, 'svg')
            for icon in icons:
                if icon.get_attribute('aria-label') == 'Like':
                    icon.send_keys(Keys.RETURN)
                    break
                

        self.driver.close()


robot = InstaBot(username, password, 'programming', 5)
robot.like_all_posts()
