#!/usr/bin/env python3

import socket, sys
from datetime import datetime


#define target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print('invalid')

print('-'* 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print('-'* 50)

try:
	for port in range(20, 100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		
		if result == 0:
			print(f'Port {port} is open')
		s.close()

except KeyboardInterrupt:
	print('Exiting program')
	sys.exit()

except socket.gaierror:
	print('hostname could not be resolved')
	sys.exit()

except socket.error:
	print('could not connect to server')
	sys.exit()

