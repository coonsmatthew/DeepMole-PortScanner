#!/usr/bin/env python
import socket
import subprocess
import sys
import threading
from threading import Thread
import random

#Set Openports variable, this will be populated by the functions that run through ports. There are 66 functions in all
openports = []

#Run through the functions that make up this script, there are 66 functions, each one will scan 999 ports in random order for the range that it has been assigned
#Each variable appends any open ports that it finds to the "openports" variable that is set above, this is then echoed out at the end of the script
def ports1():
	for port in random.sample(range(1,1000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports2():
	for port in random.sample(range(1001,2000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports3():
	for port in random.sample(range(2001,3000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports4():
	for port in random.sample(range(3001,4000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
		
def ports5():
	for port in random.sample(range(4001,5000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports6():
	for port in random.sample(range(5001,6000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports7():
	for port in random.sample(range(6001,7000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports8():
	for port in random.sample(range(7001,8000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports9():
	for port in random.sample(range(8001,9000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports10():
	for port in random.sample(range(9001,10000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports11():
	for port in random.sample(range(10001,11000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports12():
	for port in random.sample(range(11001,12000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
		
def ports13():
	for port in random.sample(range(12001,13000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports14():
	for port in random.sample(range(13001,14000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports15():
	for port in random.sample(range(14001,15000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports16():
	for port in random.sample(range(15001,16000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports17():
	for port in random.sample(range(16001,17000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports18():
	for port in random.sample(range(17001,18000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports19():
	for port in random.sample(range(18001,19000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports20():
	for port in random.sample(range(19001,20000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
		
def ports21():
	for port in random.sample(range(20001,21000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports22():
	for port in random.sample(range(21001,22000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports23():
	for port in random.sample(range(22001,23000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports24():
	for port in random.sample(range(23001,24000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports25():
	for port in random.sample(range(24001,25000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports26():
	for port in random.sample(range(25001,26000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports27():
	for port in random.sample(range(26001,27000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports28():
	for port in random.sample(range(27001,28000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
		
def ports29():
	for port in random.sample(range(28001,29000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports30():
	for port in random.sample(range(29001,30000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports31():
	for port in random.sample(range(30001,31000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports32():
	for port in random.sample(range(31001,32000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports33():
	for port in random.sample(range(32001,33000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports34():
	for port in random.sample(range(33001,34000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports35():
	for port in random.sample(range(34001,35000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports36():
	for port in random.sample(range(35001,36000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
		
def ports37():
	for port in random.sample(range(36001,37000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports38():
	for port in random.sample(range(37001,38000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports39():
	for port in random.sample(range(38001,39000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports40():
	for port in random.sample(range(39001,40000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports41():
	for port in random.sample(range(40001,41000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports42():
	for port in random.sample(range(41001,42000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports43():
	for port in random.sample(range(42001,43000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports44():
	for port in random.sample(range(43001,44000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
		
def ports45():
	for port in random.sample(range(44001,45000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports46():
	for port in random.sample(range(45001,46000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports47():
	for port in random.sample(range(46001,47000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports48():
	for port in random.sample(range(47001,48000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports49():
	for port in random.sample(range(48001,49000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports50():
	for port in random.sample(range(49001,50000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports51():
	for port in random.sample(range(50001,51000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports52():
	for port in random.sample(range(51001,52000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
		
def ports53():
	for port in random.sample(range(52001,53000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports54():
	for port in random.sample(range(53001,54000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports55():
	for port in random.sample(range(54001,55000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports56():
	for port in random.sample(range(55001,56000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports57():
	for port in random.sample(range(56001,57000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports58():
	for port in random.sample(range(57001,58000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports59():
	for port in random.sample(range(58001,59000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports60():
	for port in random.sample(range(59001,60000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
		
def ports61():
	for port in random.sample(range(60001,61000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports62():
	for port in random.sample(range(61001,62000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports63():
	for port in random.sample(range(62001,63000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports64():
	for port in random.sample(range(63001,64000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()

def ports65():
	for port in random.sample(range(64001,65000), 999):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(sockettimeout)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			openports.append(format(port))
		sock.close()
			
def ports66():
	for port in random.sample(range(65001,65535), 534):
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
	
	#Set all of the functions to run as threads, aka concurrently 
	p1 = Thread(target = ports1)
	p2 = Thread(target = ports2)
	p3 = Thread(target = ports3)
	p4 = Thread(target = ports4)
	p5 = Thread(target = ports5)
	p6 = Thread(target = ports6)
	p7 = Thread(target = ports7)
	p8 = Thread(target = ports8)
	p9 = Thread(target = ports9)
	p10 = Thread(target = ports10)
	p11 = Thread(target = ports11)
	p12 = Thread(target = ports12)
	p13 = Thread(target = ports13)
	p14 = Thread(target = ports14)
	p15 = Thread(target = ports15)
	p16 = Thread(target = ports16)
	p17 = Thread(target = ports17)
	p18 = Thread(target = ports18)
	p19 = Thread(target = ports19)
	p20 = Thread(target = ports20)
	p21 = Thread(target = ports21)
	p22 = Thread(target = ports22)
	p23 = Thread(target = ports23)
	p24 = Thread(target = ports24)
	p25 = Thread(target = ports25)
	p26 = Thread(target = ports26)
	p27 = Thread(target = ports27)
	p28 = Thread(target = ports28)
	p29 = Thread(target = ports29)
	p30 = Thread(target = ports30)
	p31 = Thread(target = ports31)
	p32 = Thread(target = ports32)
	p33 = Thread(target = ports33)
	p34 = Thread(target = ports34)
	p35 = Thread(target = ports35)
	p36 = Thread(target = ports36)
	p37 = Thread(target = ports37)
	p38 = Thread(target = ports38)
	p39 = Thread(target = ports39)
	p40 = Thread(target = ports40)
	p41 = Thread(target = ports41)
	p42 = Thread(target = ports42)
	p43 = Thread(target = ports43)
	p44 = Thread(target = ports44)
	p45 = Thread(target = ports45)
	p46 = Thread(target = ports46)
	p47 = Thread(target = ports47)
	p48 = Thread(target = ports48)
	p49 = Thread(target = ports49)
	p50 = Thread(target = ports50)
	p51 = Thread(target = ports51)
	p52 = Thread(target = ports52)
	p53 = Thread(target = ports53)
	p54 = Thread(target = ports54)
	p55 = Thread(target = ports55)
	p56 = Thread(target = ports56)
	p57 = Thread(target = ports57)
	p58 = Thread(target = ports58)
	p59 = Thread(target = ports59)
	p60 = Thread(target = ports60)
	p61 = Thread(target = ports61)
	p62 = Thread(target = ports62)
	p63 = Thread(target = ports63)
	p64 = Thread(target = ports64)
	p65 = Thread(target = ports65)
	p66 = Thread(target = ports66)
	
	#Start all of the threads :)
	p1.start()
	p2.start()
	p3.start()
	p4.start()
	p5.start()
	p6.start()
	p7.start()
	p8.start()
	p9.start()
	p10.start()
	p11.start()
	p12.start()
	p13.start()
	p14.start()
	p15.start()
	p16.start()
	p17.start()
	p18.start()
	p19.start()
	p20.start()
	p21.start()
	p22.start()
	p23.start()
	p24.start()
	p25.start()
	p26.start()
	p27.start()
	p28.start()
	p29.start()
	p30.start()
	p31.start()
	p32.start()
	p33.start()
	p34.start()
	p35.start()
	p36.start()
	p37.start()
	p38.start()
	p39.start()
	p40.start()
	p41.start()
	p42.start()
	p43.start()
	p44.start()
	p45.start()
	p46.start()
	p47.start()
	p48.start()
	p49.start()
	p50.start()
	p51.start()
	p52.start()
	p53.start()
	p54.start()
	p55.start()
	p56.start()
	p57.start()
	p58.start()
	p59.start()
	p60.start()
	p61.start()
	p62.start()
	p63.start()
	p64.start()
	p65.start()
	p66.start()
	
	# Wait until all of the threads are finished before continuing on with the script
	p1.join()
	p2.join()
	p3.join()
	p4.join()
	p5.join()
	p6.join()
	p7.join()
	p8.join()
	p9.join()
	p10.join()
	p11.join()
	p12.join()
	p13.join()
	p14.join()
	p15.join()
	p16.join()
	p17.join()
	p18.join()
	p19.join()
	p20.join()
	p21.join()
	p22.join()
	p23.join()
	p24.join()
	p25.join()
	p26.join()
	p27.join()
	p28.join()
	p29.join()
	p30.join()
	p31.join()
	p32.join()
	p33.join()
	p34.join()
	p35.join()
	p36.join()
	p37.join()
	p38.join()
	p39.join()
	p40.join()
	p41.join()
	p42.join()
	p43.join()
	p44.join()
	p45.join()
	p46.join()
	p47.join()
	p48.join()
	p49.join()
	p50.join()
	p51.join()
	p52.join()
	p53.join()
	p54.join()
	p55.join()
	p56.join()
	p57.join()
	p58.join()
	p59.join()
	p60.join()
	p61.join()
	p62.join()
	p63.join()
	p64.join()
	p65.join()
	p66.join()
	
	#Sort the results in int order and print them for the user to see
	openports.sort(key=int)
	for port in openports:
		print "Open Port: " + port
