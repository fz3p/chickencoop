# coding: utf8
#!/usr/bin/env python3

import RPi.GPIO as gpio
import datetime
import time
import logging

TIME_UP = 45
TIME_DOWN = 36
FILENAME = "/home/pi/chickencoop/status.txt"
LOGFILE = "/home/pi/chickencoop/chicken.log"


def init():
	gpio.setmode(gpio.BCM)
	gpio.setwarnings(False)
	gpio.setup(17, gpio.OUT)
	gpio.setup(22, gpio.OUT)
	logging.basicConfig(filename="chicken.log", level=logging.DEBUG, format="%(asctime)s — %(name)s — %(levelname)s — %(message)s")

	
def read_status():
	file = open(FILENAME, "r")
	status = file.readline()
	print(status)
	file.close()
	return(status)


def write_status( STATUS ):
	file = open(FILENAME, "w")
	file.write(STATUS)
	file.close()


def open_door():
	if read_status() == "Closed":
		print("Status = closed")
		write_status("Opening")
		logging.info("DOOR Opening…")
		gpio.output(17, gpio.HIGH)
		gpio.output(22, gpio.LOW)
		time.sleep(TIME_UP)
		logging.info("DOOR Opened !")
		write_status("Opened")
	else:
		logging.warning("ERROR! Action OPEN but door not closed!")

		
def force_open_door():
	write_status("Opening")
	logging.info("DOOR FORCED Opening…")
	gpio.output(17, gpio.HIGH)
	gpio.output(22, gpio.LOW)
	time.sleep(TIME_UP)
	logging.info("DOOR FORCED Opened!")
	write_status("Opened")


def close_door():
	print(read_status())
	if read_status() == "Opened":
		write_status("Closing")
		logging.info("DOOR Closing…")
		gpio.output(17, gpio.LOW)
		gpio.output(22, gpio.HIGH)
		time.sleep(TIME_DOWN)
		logging.info("DOOR Closed!")
		write_status("Closed")
	else:
		logging.warning("ERROR! Action CLOSE but door not opened!")

		
def force_close_door():
	write_status("Closing")
	logging.info("DOOR FORCED Closing…")
	gpio.output(17, gpio.LOW)
	gpio.output(22, gpio.HIGH)
	time.sleep(TIME_DOWN)
	logging.info("DOOR FORCED Closed!")
	write_status("Closed")

	
def exit_door():
	gpio.cleanup()