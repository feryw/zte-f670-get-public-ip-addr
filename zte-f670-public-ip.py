#!/usr/bin/env python3
#Model : ZTE F670 V2.0
#Desc  : Force Public IP Address Assigning

import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ont_ip = "http://192.168.1.1/"
ont_user = "admin"
ont_pass = "changeme"

chrome_path = Service(executable_path='/home/user/zte-f670-get-public-ip-addr/chromedriver')
browser_options = Options()
browser_options.add_argument('headless')

while True:
 driver = webdriver.Chrome(service=chrome_path, options=browser_options)
 driver.get(ont_ip)
 driver.find_element(By.ID, "Frm_Username").click()
 driver.find_element(By.ID, "Frm_Username").send_keys(ont_user)
 driver.find_element(By.ID, "Frm_Password").send_keys(ont_pass)
 driver.find_element(By.ID, "LoginId").click()
 time.sleep(3)

 driver.switch_to.frame("mainFrame")
 driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/font").click()
 time.sleep(3)
 ip_addr = driver.find_element(By.ID, "TextPPPIPAddress0").get_attribute('value')
 logfile = open("/home/user/zte-f670-get-public-ip-addr/ip_addr.log","a")
 dt = datetime.datetime.now()
 print(dt.strftime("%Y-%m-%d %H:%M:%S") +" "+ip_addr+"\n")
 logfile.write(dt.strftime("%Y-%m-%d %H:%M:%S")+" "+ip_addr+"\n")
 while ip_addr.startswith(("10","0")):
  driver.find_element(By.ID, "mmNet").click()
  driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[3]/table[2]/tbody/tr[1]/td[2]/select/option[3]").click()
  driver.find_element(By.ID, "Frm_WBDMode").click()
  driver.find_element(By.ID, "Btn_DoEdit").click()
  time.sleep(3)
  driver.find_element(By.ID, "Frm_WBDMode").click()
  driver.find_element(By.ID, "Frm_VLANID").clear()
  driver.find_element(By.ID, "Frm_VLANID").send_keys('200')
  driver.find_element(By.ID, "Btn_DoEdit").click()
  time.sleep(10)
  driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td[2]").click()
  driver.find_element(By.XPATH,"/html/body/div[3]/div[1]/div[1]/table/tbody/tr/td/table/tbody/tr[3]/td[2]/font").click()
  time.sleep(3)
  ip_addr = driver.find_element(By.ID, "TextPPPIPAddress0").get_attribute('value')
  dt = datetime.datetime.now()
  print(dt.strftime("%Y-%m-%d %H:%M:%S") +" "+ip_addr+"\n")
  logfile.write(dt.strftime("%Y-%m-%d %H:%M:%S")+" "+ip_addr+"\n")
  time.sleep(5)
 driver.quit()
 logfile.close()
 time.sleep(30)
