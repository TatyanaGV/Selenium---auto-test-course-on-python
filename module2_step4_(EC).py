import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR")
    )

button=browser.find_element_by_id("book")
button.click()

element1 = browser.find_element_by_id("input_value")
x = element1.text
y=calc(x)

print(y)
input1=browser.find_element_by_id("answer")
input1.send_keys(y)

button2 = browser.find_element_by_id("solve")
button2.click()  
