#!/usr/local/bin/python3

import signal
import socket
import logging
import sys

import ibeacon

# set up logging
logging_level = 'DEBUG'		
logging.basicConfig(
	filename='log',
	level=logging_level,
	format='%(asctime)-12s | %(levelname)-8s | %(name)s | %(message)s',
	datefmt='%d/%m/%y, %H:%M:%S'
)

# parse hostname to bind to from argument if supplied, otherwise default
# to 'localhost'
try:
	hostname = sys.argv[1]
except IndexError:
	hostname = 'localhost'

# catch Ctrl+C and call stop() method		
def exit_handler(signal, frame):
	scanner.stop()
signal.signal(signal.SIGINT, exit_handler)

"""
Start server to scan for ibeacon advertisements and pass to clients
host is the server IP address to bind to. 'localhost' is the default which
means only clients on the same computer can connect. Use '0.0.0.0' if you
want the server to be accesible from the outside.
When running on Linux, the server process must be running as root in order to
access the hci (bluetooth) channel. It may also be necessary to diable a 
currently running bluez daemon with `service bluetooth stop`.
"""

scanner = ibeacon.Scanner()
scanner.start(hostname)
