# MNTAjaleidmine
Maanteeameti sõidueksamiaegade leidmis programm

- enne scripti kasutamist vaata, et kõik package'id oleks tõmmatud (requirements.txt) command on: pip install -r requirements.txt peab jooksutama samas directorys kus on requirements file
- script kasutab chrome'i, on vaja tõmmata enda Chrome versiooni chromedriver (veidi vanemad: https://chromedriver.chromium.org/downloads kõige uuem: https://googlechromelabs.github.io/chrome-for-testing/)
- Scriptis sees on vaja muuta variableid: email kuhu see saadab emaili (võib olla mitu), email kust see saadab ja selle username ja pass, praeguse registreeritud soiduaja kuupaev.
- Kui panna script tööle siis vaja manuaalselt sisse logida mnt lehel. kui oled sisselogitud siis python terminalis vajuta enter. Edasi teeb automaatselt enamasti, vb peab captchat täitma.
- Kui see leiab aja siis see saadab emaili ja arvuti mängib seda audiofaili, mis kaasas on
- Vaata, et email ei lähe spam folderisse
