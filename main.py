import requests
import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://web.whatsapp.com/")
input("Hit enter after verifying!")

chat_xpath = "//*[@id=\"pane-side\"]/div[2]/div/div/div[11]"

chat_name_el = driver.find_element(By.XPATH, chat_xpath)
chat_name_el.click()
pdb.set_trace()

input("Hit enter to send the message")

text_box_xpath = "//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"
send_msg_btn_xpath = "//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button"

for i in range():
    text_box_el = driver.find_element(By.XPATH, text_box_xpath)
    response = requests.get("https://api.chucknorris.io/jokes/random")
    message = response.json()["value"]
    text_box_el.send_keys(message)
    send_msg_btn_el = driver.find_element(By.XPATH, send_msg_btn_xpath)
    send_msg_btn_el.click()

print("End of the script!")

