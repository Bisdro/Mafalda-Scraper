from  selenium import webdriver
import time
from selenium.webdriver.common.by import By
textoMafalda = open("textos mafalda.txt","a",encoding='UTF-8')
driver =webdriver.Chrome("./chromedriver.exe")
driver.get("https://stryptor.herokuapp.com/mafalda/01/001/")
while True:
    texto = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/main/div/div[3]').text
    textoMafalda.write(texto)
    time.sleep(0.5)
    boton = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div/main/div/div[1]/ol/li[4]/a',)
    boton.click()
    if driver.title =="Mafalda Inédita-084":
        break

textoMafalda.close()
