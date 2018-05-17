from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


#browser = webdriver.Chrome()

def visitAWebsiteAndGetSomeData():
    #define where webdriver is
    browser = webdriver.Chrome( "D:\Coding\Python\Selenium Bot Fiddle\Dependencies\chromedriver.exe")
    #define page to load
    print(browser.get('http://ckl-it.de/'))
    #select an element by xpath
    text = browser.find_element_by_xpath('//*[@id="masthead"]/div/h1/a')
    print (text)
    #select an attribute from an element
    print (text.get_attribute("href"))
    #click an element we got by calling browser.find_element_by_xpath
    text.click()

def openMultiplePagesInMultipleTABS():
    #define where webdriver is
    browser = webdriver.Chrome( "D:\Coding\Python\Selenium Bot Fiddle\Dependencies\chromedriver.exe")
    print(browser.get('http://ckl-it.de/'))
    text = browser.find_element_by_xpath('//*[@id="masthead"]/div/h1/a')
    print (text)
    #select an attribute from an element
    print (text.get_attribute("href"))
    #click an element we got by calling browser.find_element_by_xpath
    browser.execute_script("window.open('https://www.google.com');")
    browser.execute_script("window.open('https://www.google.com');")
    browser.execute_script("window.open('https://www.google.com');")


openMultiplePagesInMultipleTABS()