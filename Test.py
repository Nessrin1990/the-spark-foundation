# import required packages
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait

#path webdriver
path = 'C:/Users/DELL/Desktop/chromedriver'
#driver = webdriver.Chrome(path)
s = Service(path)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.maximize_window()
# Open URL
driver.get('https://www.thesparksfoundationsingapore.org/')

time.sleep(2)
#programs
driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[3]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[3]/ul/li[4]/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[5]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[5]/div/a').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[1]/div/div')
time.sleep(2)



#join Us
driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[5]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="link-effect-3"]/ul/li[5]/ul/li[1]').click()
time.sleep(2)
#subscribe to join us
name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]')
name.send_keys("nesrineAzaiez")
time.sleep(2)

mail = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]')
mail.send_keys("Nesrine.azaiez6@example.com")
time.sleep(2)

function = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]').text
time.sleep(2)
function1 = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/select/option[5]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[2]/div/form/input[3]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[3]').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[3]/ul/li/a').click()
time.sleep(10)


