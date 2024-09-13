from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import warnings
warnings.filterwarnings('ignore')
from inspect import currentframe, getframeinfo
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import timeit
import time
import subprocess

start = timeit.default_timer()
##  define global variables for logging
app_name = 'APPLE'
page_name = 'certificates'
subpage_name = ''
action = ''
####
cf = currentframe()
filename = getframeinfo(cf).filename
cdriver = "./chromedriver_mac64/chromedriver"
chromeOptions = Options()
chromeOptions.add_argument("user-data-dir=./Default")
chromeOptions.add_argument("--headless")
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--window-size=1660,1050')
chromeOptions.add_argument("--ignore-certificate-errors")
chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--disable-infobars')
browser = webdriver.Chrome(cdriver,options=chromeOptions)
browser.set_window_position(-5, 0)
browser.maximize_window()
subpage_name="Login"
URL = "https://developer.apple.com/account"
action='URL'
browser.get(URL)
browser.get(URL)
time.sleep(7)
browser.switch_to.frame('aid-auth-widget-iFrame')
time.sleep(5)
browser.find_element_by_xpath('//*[@id="account_name_text_field"]').send_keys("user@email.com")
time.sleep(1)
browser.find_element_by_xpath('//*[@id="sign-in"]').click()
time.sleep(2)
continue_button = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "continue-password"))
)
continue_button.click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="password_text_field"]').send_keys("$PASSWORD")
time.sleep(1)
browser.find_element_by_xpath('//*[@id="sign-in"]').click()
time.sleep(5)

#2fa set two_fa vars
try:
    script_path = './get-2fa.sh'
    result = subprocess.run([script_path], capture_output=True, text=True, shell=True)
    two_fa = result.stderr.strip().replace(' ','')
    #if two_fa:
    #    print("osascript 2fa:")
    #    print(two_fa)
finally:
    time.sleep(3)

try:
    # find 'Two-Factor Authentication'
    try:
        if browser.find_element(By.XPATH, "//*[contains(text(), 'Two-Factor Authentication')]"):
            #print("Two-Factor Authentication metni bulundu.")
            input_xpath = '//*[@id="stepEl"]/div/hsa2-sk7/div/div[2]/div[1]/div/div/input[1]'
            input_element = browser.find_element(By.XPATH, input_xpath)
            input_element.send_keys(two_fa) 
            #print(f"'{input_xpath}' xpath'ine '{two_fa}' değeri yazıldı.")
            time.sleep(4)
            button_element = browser.find_element(By.XPATH, '//*[@id="stepEl"]/div/hsa2-sk7/div/div[2]/fieldset/div/div[2]/button2]')
            button_element.click()
            #print("click trust xpath")
    except NoSuchElementException:
        #print("Not found 'Two-Factor Authentication' text")
        time.sleep(0)
finally:
    time.sleep(6)

#return browser get myacinfo
browser.get("https://developer.apple.com/account/")
cookies = browser.get_cookies()

myacinfo_value = None
for cookie in cookies:
    if cookie["name"] == "myacinfo":
        myacinfo_value = cookie["value"]
        break

# Değerleri kontrol edin
if myacinfo_value:
    print(myacinfo_value)
else:
    print("myacinfo değeri bulunamadı.")

browser.close()
browser.quit()