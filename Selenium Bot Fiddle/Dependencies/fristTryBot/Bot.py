from selenium import webdriver
from bs4 import BeautifulSoup

from html.parser import HTMLParser

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#browser = webdriver.Chrome()
browser = webdriver.Chrome( "D:\Coding\Python\Selenium Bot Fiddle\Dependencies\chromedriver.exe")
browser.get('https://www.okcupid.com/')
signIn = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[2]/button')

signIn.click()
#enter Name
accNameInput = browser.find_element_by_xpath('//*[@id="login_username"]')
accNameInput.send_keys("ckloanyt@gmail.com")
#enter password
passwordInput = browser.find_element_by_xpath('//*[@id="login_password"]')
passwordInput.send_keys("notabot123")

#submit acc info
submitLoginButton = browser.find_element_by_xpath('//*[@id="sign_in_button"]')
submitLoginButton.click()

browser.get("https://www.okcupid.com/match")
browser.refresh()






#TODO get Every user ID on the Page , then visist Each page and send a message
# Plan B, maye Ditch jsoup and implement everything using Selenium
# Since User IDs dont Map to profiles, Open each Profile in a new Tab by clicking it and then send a message
# would also seem more natural to OKC'S server if the user is actually clicking the link  and having a CRF tag , instead of just ivisting a page directly by entering url

#get the results
result_Cards = browser.find_element_by_xpath('//*[@id="match_results"]/span[1]/div')
print (result_Cards.get_attribute("innerHTML"))

soup = BeautifulSoup (result_Cards.get_attribute("innerHTML"),"html.parser")

print ("PRE LOOP" + str(soup.body))

for div in soup.find_all("div", "match_card") :
    print (str(div))
    print(str(div.id))
    #print (str(div))
    #print (str(div.attr("id")))