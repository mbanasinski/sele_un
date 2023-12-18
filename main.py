import undetected_chromedriver as uc
import time


driver = uc.Chrome()
driver.get('https://moneysmart.gov.au/find-unclaimed-money')
time.sleep(1000)
