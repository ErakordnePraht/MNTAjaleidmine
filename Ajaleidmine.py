from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from datetime import datetime
import _thread
import time
import smtplib
import winsound

global saadaEmail

idpin = "XXXX"
emailto = ["emailto@gmail.com"]
emailfrom = "emailfrom@gmail.com"
emailpass = "emailfrom_pass"
#Hetkel registreeritud soiduaeg
currentDate = "25.09.2019"

saadaEmail = True
fox = webdriver.Chrome()
fox.get("https://eteenindus.mnt.ee/main.jsf")
input("sisse logitud? ")

while True:
    try:
        time.sleep(5)
        element = fox.find_element(By.ID, "j_idt140:j_idt159")
        element.click()
        time.sleep(2)
        element = fox.find_element(By.XPATH, "//*[text()='Kus saab kõige kiiremini eksamile?']")
        element.click()
        time.sleep(3)
        element = fox.find_element(By.ID, "varaseimadEksamiajadForm").find_element(By.TAG_NAME, "ul")
        print(element)
        varaseimAeg = element.find_element(By.XPATH, ".//strong").text
        print(datetime.now().time())
        print(element.text)
        print(varaseimAeg)

        if varaseimAeg != currentDate and saadaEmail == True:
            #Saadab emaili et uus aeg on
            print("Email saadetud")
            winsound.PlaySound("found.wav", winsound.SND_FILENAME)
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(emailfrom, emailpass)
            emailText = """To: {}
            Subject: {}\n
            Uus soiduaeg tuli:\n{}
            """.format(emailto, varaseimAeg, ascii(element.text))
            server.sendmail(
            emailfrom, 
            emailto, 
            emailText)
            server.quit()

            saadaEmail = False
        elif varaseimAeg == currentDate and saadaEmail == False:
            #Saadab emaili, et koht võeti ära
            print("Email saadetud")
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(emailfrom, emailpass)
            server.sendmail(
            emailfrom, 
            emailto, 
            "Soiduaeg voeti ara")
            server.quit()
            saadaEmail = True
        time.sleep(55)
        fox.get("https://eteenindus.mnt.ee/main.jsf")
    except:
        print("crash")
        fox.get("https://eteenindus.mnt.ee/main.jsf")
        time.sleep(5)
        #pass
