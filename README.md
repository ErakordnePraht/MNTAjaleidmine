# MNTAjaleidmine
Maanteeameti sõidueksamiaegade leidmis programm

- Ühenda ID kaart arvutiga ja kui sisse logitud võib ära võtta
- Kasutusel on Python 3.7
- enne scripti kasutamist vaata, et kõik package'id oleks tõmmatud (requirements.txt)
- script kasutab chrome'i, arvatavasti chrome version 75 (kui ei tööta siis tõmba enda versioonile chromedriver)
- emaili saatmiseks on vaja enne gmailis enable'ida "allow less secure apps": https://support.google.com/accounts/answer/6010255
- Scriptis sees on vaja muuta variableid: email kuhu see saadab emaili (võib olla mitu), email kust see saadab ja selle pass, praeguse registreeritud soiduaja kuupaev ja idkaardi pin1 (idkaart peab ühendatud olema, kui jooksutad scripti, kuid kui on sisse logitud võid ära võtta). Võib disableida automaatne id-kaardi logimine ja muuta see manuaalseks (panga või mobiil-id või miski)
- Kui see leiab aja siis see saadab emaili ja arvuti mängib seda audiofaili, mis kaasas on
- Vaata, et email ei lähe spam folderisse