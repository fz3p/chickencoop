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
wget http://risacher.org/sunwait/sunwait-20041208.tar.gz

### extraction et décompression
tar -xzf sunwait-20041208.tar.gz

### compilation
cd sunwait-20041208
make

### ensuite pour le test : 
./sunwait -p 43.729N 79.292W
