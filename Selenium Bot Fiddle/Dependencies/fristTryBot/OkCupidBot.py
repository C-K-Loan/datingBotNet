from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
from selenium.common.exceptions import NoSuchElementException

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
#accNameInput.send_keys("ckloanyt@gmail.com")

#enter password
passwordInput = browser.find_element_by_xpath('//*[@id="login_password"]')
#passwordInput.send_keys("notabot123")

#submit acc info
submitLoginButton = browser.find_element_by_xpath('//*[@id="sign_in_button"]')
submitLoginButton.click()

browser.get("https://www.okcupid.com/match")
print("Refresing ")
browser.refresh()




#message_15306878755175798577

#TODO get Every user ID on the Page , then visist Each page and send a message
# Plan B, maye Ditch jsoup and implement everything using Selenium
# Since User IDs dont Map to profiles, Open each Profile in a new Tab by clicking it and then send a message
# would also seem more natural to OKC'S server if the user is actually clicking the link  and having a CRF tag , instead of just ivisting a page directly by entering url

#get the div with the  user profiles in them
print("getting result cards")
result_Cards = browser.find_element_by_xpath('//*[@id="match_results"]/span[1]/div')

print ("got result cards")

#Prepare the HTML
soup = BeautifulSoup (result_Cards.get_attribute("innerHTML"), "html.parser")


# THIS GETS US ALLL THE PROFILE URL's ON THE PAGE
#for url in soup.find_all('a'):
#    print(url.get('href'))





#Visit Profile

# SELECTOR FÜR DAS MSG TEXT INPUT FIELD .compose-textarea-wrapper>[id]>textarea[id]
urls = soup.find_all('a')
urlsNoDuplicates = set(urls)
#for url in urlsNoDuplicates :
#    print("one day gonna visiting" + str(url))

message = " Hey intresting profile ;)"
wt = 10#Waittime
for url in urlsNoDuplicates :
    print("I want to visit : " + 'https://www.okcupid.com/' + str(url.get('href')))
    browser.get('https://www.okcupid.com'+ str(url.get('href')))
#TODO  add exception, incase we fail to log in -> wait 5 mikn want retry
#TODO alternative button selector! -> sometimes button selector s dosent work -> add this selecotr ->  #global_messaging_container > div.global_messaging.no_messages.with_user_instruction > form > button
#TODO auto restart!

    browser.implicitly_wait(2)
    try:

        print("Cliking like button...")
        browser.implicitly_wait(wt)
        browser.find_element_by_xpath('//*[@id="like-button"]').click()

        print("Sending message...")
        browser.implicitly_wait(wt)
        browser.find_element_by_css_selector(".compose-textarea-wrapper>[id]>textarea[id]").send_keys("Hey what is up!")

        print("Clicking send..")
        browser.implicitly_wait(wt)
        browser.find_element_by_css_selector("#global_messaging_container > div.global_messaging.initial-render.no_messages.with_user_instruction > form > button").click()

    except NoSuchElementException:

        print("PROFILE ALREADYL LIKED!!.... clicking message directy..")

        print("clicking message button..")
        browser.implicitly_wait(wt)
        browser.find_element_by_css_selector("#profile_actions > div > div > span > div > div > button.profile-buttons-actions-action.profile-buttons-actions-message").click()

        print("Sending message...")
        browser.implicitly_wait(wt)
        browser.find_element_by_css_selector(".compose-textarea-wrapper>[id]>textarea[id]").send_keys("Hey what is up!")

        print("Clicking send..")
        browser.implicitly_wait(wt)
        browser.find_element_by_css_selector("#global_messaging_container > div.global_messaging.initial-render.no_messages.with_user_instruction > form > button").click()


    print("done with message loop")
    browser.implicitly_wait(2)
#send message
#backup withouth exception implemntation
#print("No element found")
#print("Cliking like button...")
#browser.find_element_by_xpath('//*[@id="like-button"]').click()
#print("Sending message...")
#browser.find_element_by_css_selector(".compose-textarea-wrapper>[id]>textarea[id]").send_keys("Hey what is up!")
#print("Clicking send..")
#browser.find_element_by_css_selector("#global_messaging_container > div.global_messaging.initial-render.no_messages.with_user_instruction > form > button").click()

#TODO ADD FUNCTIONS FOR THIS SHIT
# TODO WHILE PAGE NOT MATCH PAGE; KEEP REFRESHING AND RELOGGING!
# TODO ADD CHECK IF LIKE BUTTON IS ALREADY THERE
