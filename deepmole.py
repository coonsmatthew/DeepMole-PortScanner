#!/usr/bin/env python
import socket
import subprocess
import sys
import threading
from threading import Thread
from multiprocessing.pool import ThreadPool
import random

#Set Openports variable, this will be populated by the functions that run through ports. There are 66 functions in all
openports = []

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]

# accept a list of ports, randomize it and test the port
# if the port is open append to the global openports
# this should be threadsafe since append should be an atomic operation
def ports(ports):
	for port in random.sample(ports,len(ports)):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

	
if __name__ == '__main__':
	
	#Verify that there are at least 2 arguments inserted...
	if len(sys.argv) < 3:
		sys.exit("\nPlease provide IP or DNS name and timeout window \n \nExample: #python deepmole.py 10.1.1.1 .01")
		
	#collect variables from the terminal that are needed to run the script, also set the sockettimeout variable to float
	remoteServer = sys.argv[1]
	sockettimeout = sys.argv[2]
	sockettimeout = float(sockettimeout)
	remoteServerIP  = socket.gethostbyname(remoteServer)

	#print variables selected to the end user...
	print "\nTarget: " + remoteServer + "\n"
	print "Timeout Window Selected: " + str(sockettimeout)  + "\n"
	print "Scanning, please wait... \n" 
	
        # define allports as a list of chunks of 999 numbers from 1 to 65535
        allports=list(chunks(range(1,65535),999))

        # create a threadpool with a number of workers equal to the number 
        # of chunks of ports in the list allports, then start the worker pool
        # using the ports function and allports as the list of arguments
        pool=ThreadPool(len(allports))
        pool.map(ports,allports)
	
	#Sort the results in int order and print them for the user to see
	openports.sort(key=int)
	for port in openports:
		print "Open Port: " + port
