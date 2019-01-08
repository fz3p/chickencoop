#!/usr/bin/python

from requests.auth import HTTPBasicAuth
import requests
import sys
import Adafruit_DHT
import door

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# fonction
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def maj_widget(val_url):
    requete = 'http://' + domoticz_ip + ':' + domoticz_port + val_url
    # print requete
    r = requests.get(requete, auth=HTTPBasicAuth(user, password))
    if r.status_code != 200:
        print("Erreur API Domoticz")
		
def door_status():
	url_door = '/json.htm?type=command&param=udevice&idx=' + str(domoticz_idx_door)
    url_door += '&nvalue=0&svalue='
    url_door += door.read_status()
	print(url)
	maj_widget
	
def temp_status():
	if humidity is not None and temperature is not None:
	
		# https://www.domoticz.com/wiki/Domoticz_API/JSON_URL%27s#Temperature.2Fhumidity.2Fbarometer
		# modele url : /json.htm?type=command&param=udevice&idx=IDX&nvalue=0&
		# svalue=TEMP;HUM;
		# l URL Domoticz pour le widget virtuel

		url = '/json.htm?type=command&param=udevice&idx=' + str(domoticz_idx)
		url += '&nvalue=0&svalue='
		url += str('{0:0.1f};{1:0};0').format(temperature, humidity)
		print(url)
		maj_widget(url)
	else:
		print('Probleme avec la lecture du DHT11. Try again!')
		sys.exit(1)
	

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# les parametres de Domoticz
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

domoticz_ip = ''
domoticz_port = '8080'
user = ''
password = ''
domoticz_idx = ''
domoticz_idx_door = ''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# récuperation des informations des capteurs
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# sensor est 11,22,ou 2302
# pin est le numero d la pin que vous avez cablée
# https://pinout.xyz/pinout/pin12_gpio18#
sensor = 11
pin = 18
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# envoi des données
door_status()
temp_status()



