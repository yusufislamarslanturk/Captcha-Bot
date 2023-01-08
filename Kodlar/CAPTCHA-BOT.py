from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
import time
import pytesseract
import os

username = os.getlogin()
driver = webdriver.Chrome(executable_path="C:/Users/"+username+"/Desktop/DENEME/chromedriver.exe")
driver.maximize_window()
driver.get("https://sonuc.osym.gov.tr/BelgeKontrol.aspx")

time.sleep(2)
s=driver.find_element(By.XPATH,'//div[@class="captchaImage"]/img[@src]')
pytesseract.pytesseract.tesseract_cmd = r"C:/Users/"+username+"/Desktop/yol/chromedriver.exe"

location = s.location
size = s.size
driver.save_screenshot("captcha-ss.png")
x = location['x']
y = location['y']
height = location['y']+size['height']
width = location['x']+size['width']
imgOpen = Image.open("captcha-ss.png")
imgOpen = imgOpen.crop((int(x), int(y), int(width), int(height)))
imgOpen.save("captcha-ss.png")

pytesseract.pytesseract.tesseract_cmd = r"C:/Users/"+username+"/Desktop/yol/tesseract.exe"
a=pytesseract.image_to_string(Image.open('captcha-ss.png'), lang="tur")
gir = driver.find_element(By.XPATH,'//*[@id="captchaKod"]')
gir.send_keys(a)