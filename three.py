from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import requests
import time
from anticaptchaofficial.imagecaptcha import *

web = webdriver.Chrome()
web.get("https://electoralsearch.in/#!#resultArea")

ele = web.find_element(By.XPATH, '//*[@id="continue"]')
ele.click()
last = web.find_element(By.XPATH, '//*[@id="name1"]')
last.send_keys("Srinivasan")
lastf = web.find_element(By.XPATH, '//*[@id="txtFName"]')
lastf.send_keys("Manickam")
lasta = web.find_element(By.ID,'ageList')
drp=Select(lasta)
drp.select_by_visible_text("41")
lastg = web.find_element(By.ID,'listGender')
drp=Select(lastg)
drp.select_by_value("M")
lasts = web.find_element(By.ID,'nameStateList')
drp=Select(lasts)
drp.select_by_visible_text("Tamil Nadu")
time.sleep(2)
lastd = web.find_element(By.ID,'namelocationList')
drp=Select(lastd)
drp.select_by_visible_text("Chennai")
time.sleep(3)
lastd = web.find_element(By.XPATH,'//*[@title="Select district or constituency"]')
drp=Select(lastd)
drp.select_by_visible_text("Mylapore")
ele = web.find_element(By.XPATH, '//*[@id="captchaDetailImg"]')
ele.screenshot('./image.png')
time.sleep(5)
solver = imagecaptcha()
solver.set_verbose(1)
solver.set_key("ad231592d43af231b3e8bddb2e905e88")
part = 200
acc = 25
sno= 405
# Specify softId to earn 10% commission with your app.
# Get your softId here: https://anti-captcha.com/clients/tools/devcenter
solver.set_soft_id(0)

last = web.find_element(By.XPATH, '//*[@id="txtCaptcha"]')
# while last.get_attribute("value") == "":
captcha_text = solver.solve_and_return_solution("image.png")
if captcha_text != 0:
    print("captcha text "+captcha_text)
else:
    print("task finished with error "+solver.error_code)
last.send_keys(captcha_text)
time.sleep(5)
eles = web.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div/div[1]/form/fieldset/div/div[4]/div[2]/div[2]/button')
eles.click()
time.sleep(5)
det = web.find_element(By.XPATH,'//*[@id="resultsTable"]/tbody/tr/td[1]/form/input[25]')
det.click()
time.sleep(15)
# ac = web.find_element(By.XPATH,'//*[@id="ng-app"]/body/div[4]/div/div[1]/form/table/tbody/tr[11]/td[2]')
# s = ac.getText()
print("Part no : ",part)
print("AC no : ",acc)
print("SC no : ",sno)