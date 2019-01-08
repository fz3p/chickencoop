#raspberry_0w_chickencoop

## install Debian 9

## pre-requis 
`sudo apt-get update && sudo apt-get upgrade`
`sudo apt-get install python3 RPi.GPIO`

* attribuer les bons droits aux différents fichiers 
* pour tester : `sudo python3 open_door.py` ou  `sudo python3 close_door.py`


# récupération de la température

## installation de python
`
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo apt-get update
sudo apt-get install build-essential python-dev python-openssl
sudo python setup.py install
`

## installation de pip
`
sudo apt-get upgrade
sudo apt-get install python-pip
sudo pip install requests
`

## rendre executable
`chmod +x /home/user/script/send_to_domoticz.py`

## automatisation 
`
sudo crontab -e
*/1 * * * * sudo /home/user/script/send_to_domoticz.py
`
*http://fr.wikipedia.org/wiki/Crontab*

# automatisation de l'ouverture et de la fermeture de la porte 

## installation de sunwait  
### téléchargement 
`wget http://risacher.org/sunwait/sunwait-20041208.tar.gz`

### extraction et décompression
`tar -xzf sunwait-20041208.tar.gz`

### compilation
`cd sunwait-20041208`
`make`

### ensuite pour le test : 
`./sunwait -p 47.218N -1.554W`

*modele pour le cron : example: sunwait sun up -0:15:10 38.794433N 77.069450W
This example will wait until 15 minutes and 10 seconds before the sun rises in Alexandria, VA*

ajouter sunwait à `/etc/bash.bashrc` : `PATH=$PATH:/path` 

### Pour connaitre les horaires :
d'ouverture la porte : 
`sunwait sun up -0:20:00 47.218N -1.554W`

de fermeture la porte : 
`sunwait sun donw 0:20:00 47.218N -1.554W`

### ajouter au cron 
`00 04 * * * sunwait sun up -0:20:00 47.218N -1.554W ; sudo python3 /home/pi/open_door.py`
`00 15 * * * sunwait sun down 0:20:00 47.218N -1.554W ; sudo python3 /home/pi/close_door.py`

# statut dans domoticz
*modele /json.htm?type=command&param=udevice&idx=IDX&nvalue=0&svalue=TEXT
https://www.domoticz.com/wiki/Domoticz_API/JSON_URL%27s#Text_sensor*
crééer un device virtuel (dummies) de type texte

