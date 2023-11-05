from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import keyboard



get_api_text = 'vamos consumir uma api de noticias para sempre atualizarmos a busca'


driver = webdriver.ChromiumEdge()
print('acessar site')
driver.get('https://www.bing.com/')
print('wait de 10')
driver.implicitly_wait(10)
print('localizar alvo da pesquisa')
search_box = driver.find_element(By.XPATH, "//*[@id='sb_form_q']")
print('clicar no alvo')
search_box.click()
print('esperar 2s')
time.sleep(2)
print('colar texto')
search_box.send_keys(my_text)
print('pressionar enter')
search_box.send_keys(Keys.ENTER)
time.sleep(2)


while True: 
    print('busca alvo')
    time.sleep(1)
    search_box = driver.find_element(By.XPATH, "//*[@id='sb_form_q']")
    print('apaga')
    search_box.send_keys(Keys.BACKSPACE)
    time.sleep(3)
    print('pesquisa')
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)






