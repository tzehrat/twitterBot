
from main import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



class Twitter():
    def __init__(self, username, password):
        self.browserProfile= webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en , en_US"})
        self.browser=webdriver.Chrome("chromedriver.exe", chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def sıgnIn(self):

        self.browser.get("https://twitter.com/login")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)

    def search(self,hashtag):
        self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input").click()
        a=self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input").send_keys(hashtag)
        time.sleep(2)
        a.send_keys(Keys.ENTER)
        #self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input").send_keys(hashtag).click()
        time.sleep(2)

        liste=self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[2]")
        for i in liste:
            print(i.text)





twitter=Twitter(username,password)
twitter.sıgnIn()
twitter.search("python")
