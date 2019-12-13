# coding:utf-8
from  selenium import webdriver
import  time
driver=webdriver.Chrome()
driver.maximize_window()
driver.set_window_size(1080,720)
driver.get("https://www.baidu.com")
time.sleep(3)
driver.close()