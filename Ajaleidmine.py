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

emailserver = "smtp.sendgrid.net"
emailto = ["emailto@gmail.com"]
emailfrom = "emailfrom@gmail.com"
emailusername = "apikey"
emailpass = "emailfrom_pass"
#Hetkel registreeritud soiduaeg
currentDate = "03.08.2023"

saadaEmail = True
fox = webdriver.Chrome()
fox.get("https://eteenindus.mnt.ee/main.jsf")
input("sisse logitud? (vajuta enter kui jah)")

while True:
    try:
        # Pealeht
        element = fox.find_element(By.ID, "j_idt140:j_idt159")
        element.click()

        # Juhi vaade
        time.sleep(60)
        element = fox.find_elements(By.XPATH, "//*[text()='Muuda valikut »']")[0]
        element.click()

        # Soiduaegade vaade
        time.sleep(25)
        element = fox.find_element(By.XPATH, "//*[text()='Kus saab kõige kiiremini eksamile?']")
        element.click()

        # Kiireimad soiduajad modal
        time.sleep(2)
        varaseimAegItem = fox.find_element(By.XPATH, "(//ul)[last()]/li[1]")
        varaseimAeg = varaseimAegItem.find_element(By.XPATH, ".//strong").text
        print(datetime.now().time())
        print(varaseimAegItem.text)
        print(varaseimAeg)

        if varaseimAeg != currentDate and saadaEmail == True:
            #Saadab emaili et uus aeg on
            print("Email saadetud")
            winsound.PlaySound("found.wav", winsound.SND_FILENAME)
            server = smtplib.SMTP_SSL(emailserver, 465)
            server.login(emailusername, emailpass)
            emailText = f"""From: {emailfrom}\nTo: {', '.join(emailto)}\nSubject: {varaseimAeg}\n
            Uus soiduaeg tuli:\n{ascii(varaseimAegItem.text)}
            """
            server.sendmail(
            emailfrom, 
            emailto, 
            emailText)
            server.quit()

            saadaEmail = False
        elif varaseimAeg == currentDate and saadaEmail == False:
            #Saadab emaili, et koht võeti ära
            print("Email saadetud - soiduaeg voeti ara")
            server = smtplib.SMTP_SSL(emailserver, 465)
            server.login(emailusername, emailpass)
            emailText = f"""From: {emailfrom}\nTo: {', '.join(emailto)}\nSubject: Soiduaeg voeti ara\n
            """
            server.sendmail(
            emailfrom, 
            emailto, 
            emailText)
            server.quit()

            saadaEmail = True
        time.sleep(60)
        print()
        fox.get("https://eteenindus.mnt.ee/main.jsf")
    except Exception as e:
        print("crash")
        fox.get("https://eteenindus.mnt.ee/main.jsf")
        time.sleep(5)
        #pass
