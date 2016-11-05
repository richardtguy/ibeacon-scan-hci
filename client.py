#!/usr/local/bin/python3

import signal
import sys
import logging

import ibeacon

# set up logging
logging_level = 'DEBUG'		
logging.basicConfig(
	filename='log',
	level=logging_level,
	format='%(asctime)-12s | %(levelname)-8s | %(name)s | %(message)s',
	datefmt='%d/%m/%y, %H:%M:%S'
)

# parse hostname from argument if supplied, otherwise default to 'localhost'
try:
	hostname = sys.argv[1]
except IndexError:
	hostname = 'localhost'

def exit_handler(signal, frame):
	print('Exiting...')
	exit()
signal.signal(signal.SIGINT, exit_handler)

def message_handler(msg):
	print("UUID: %s, Major: %s, Minor: %s, RSSI: %s" % (msg['UUID'], msg['Major'], msg['Minor'], msg['RSSI']))

server_address = (hostname, 9999)
client = ibeacon.Client(server_address, on_message=message_handler)
