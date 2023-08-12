from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

service = ChromeService()
driver = webdriver.Chrome(service=service)

keyword = "아바타 물의 길"
serchUrl = f"https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bkEw&pkid=68&os=1808619&qvt=0&query={keyword} 평점"

driver.get(serchUrl)

spoilerButton = driver.find_element(By.XPATH, '//*[@id="main_pack"]/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[2]/button/span[1]/span[1]')

spoilerButton.click()

time.sleep(5)