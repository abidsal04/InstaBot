from selenium import webdriver #pip install selenium
from selenium.webdriver.common.keys import Keys
import random
import os
import time

class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        #Open chrome browser
        self.driver = webdriver.Chrome('./chromedriver.exe')
        
        
    def login(self):

        #Open Instagram
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)

        #Auto type username and password
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)

        #Click on login button
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
        time.sleep(3)

        #To remove the popup for notification
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]').click()
                                           

    def like(self, hashtag):

        #Search the given Hashtag
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag +'/')
        time.sleep(5)

        #Open the thumbnail
        open_thumbnail = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div')
        open_thumbnail.click()
        time.sleep(2)

        try:
            for x in range(1,10):

                #Click on like button
                button_like = driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span')
                button_like.click()
                time.sleep(3)
                
                #Clickon comment button
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[2]/button/span').click()

                #Write in comment box
                comments = self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/textarea')
                comments.send_keys(random.choice(['Nice', 'Superb', 'Cool', 'Beautiful', 'Awesome', 'Great', 'Cute', 'Sweet']))
                time.sleep(2)

                #Click on Post
                self.driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/section[3]/div/form/button').click()
                time.sleep(10)

                #click for next pic
                driver.find_element_by_link_text('Next').click()
                time.sleep(5)
                
                x+=1

        except Exception as e:
            print(e)



if __name__ ==  "__main__":
    ig_bot = InstaBot('Enter_Username', 'Password')
    ig_bot.login()
    time.sleep(3)
    ig_bot.like("hashtag_name")