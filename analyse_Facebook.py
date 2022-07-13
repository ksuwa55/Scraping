#import selenuum and the necessary opitions to login to FB
import selenium
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

#importing time libraries to add wait time
from datetime import datetime
from time import sleep

#import beautiful soup
from bs4 import BeautifulSoup

# to create csv file where we'll scrape the contatnte
import pandas as pd

#Google Translator
from googletrans import Translator

# the options functionelity to disable notifications
chrome_options = Options()
# disable notifications
chrome_options.add_argument("--disable-notifications")


content_list = []
time_list = []
name_list = []

driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

driver.get("https://www.facebook.com")
driver.maximize_window()
sleep(2)

#accept cookies
cookies = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]')))

email=driver.find_element_by_id("email")
email.send_keys("klklklkl063055@gmail.com")
password=driver.find_element_by_id("pass")
password.send_keys("kazuki0630")
sleep(1)
login=driver.find_element_by_name("login")
login.click()
sleep(2)
driver.get("https://www.facebook.com/groups/2460936690587195?sorting_setting=CHRONOLOGICAL")
sleep(4)

tr = Translator()

while True:
    soup=BeautifulSoup(driver.page_source,"html.parser")
    all_posts=soup.find_all("div",{"class":"du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"})

    for post in all_posts:
        try:
            content=post.find("span",{"class":"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id hzawbc8m"})
            content=content.text # to text
            content=tr.translate(content,src='vi',dest='en').text # Vietnamese to English
        except:
            content="not found"
        print(content)

        content_list.append(content)
        df=pd.DataFrame({"content":content_list})
        df.drop_duplicates(subset="content", keep="first", inplace = True)

        df.to_excel("facebook_data.xlsx")

        if df.shape[0]>10
            break

    if df.shape[0]>10:
        break

    sleep(5)
    y=500
    for timer in range(0,25):
        driver.execute_script("window.scrollTo(0, "+ str(y) + ")")
        y += 500
        sleep(3)