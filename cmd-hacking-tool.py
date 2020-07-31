import cmd
import os
import socket
import time
from lib.urlparsing import *

def socket_full(the_socket, timeout=2):

	#Stop the blocking

	the_socket.setblocking(0)

	#Set the data values for later

	data = ''
	totaldata = []

	#Create a time value

	begin = time.time()

	while 1:

		if totaldata and time.time()-begin > timeout:
			break

		#Have a little more timeout

		elif time.time()-begin > timeout*2:
			break

		try:
			data = the_socket.recv(4096)

			if data:
				#Add the data to a list
				totaldata.append(data.decode())
				#Reset the time value
				begin = time.time()

			else:
				#Have a gap to get data
				time.sleep(0.05)

		except:
			pass

	return(''.join(totaldata))

class Terminal(cmd.Cmd):

	#Set intro and a prompt

	prompt = '(Hacking tools)@Tasaddar:// '
	intro = 'Welcome to the hacking toolbox!!! Use ? for commands.\n Send command supports http only currently.\n\n '
	
	#Create a default command response

	def default(self, line):
		os.system(line)

	#Test the URL parsing

	def do_Send(self, url):

		#Extra argument handling

		args = re.split(r"\s", url)

		if ("-h" in args) or ("--help" in args):
			print("Working on the file :)")
			return

		#Set url from args

		url = args[0]
		'Send -h for more'

		if not 'method' in locals():
			method = 'GET'

		try:

			#Create the http request

			req = "%s %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (method, HTTPParse.filepath(url), HTTPParse.host(url))
			
			#Create the socket

			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
				sock.connect((str(HTTPParse.host(url)), int(HTTPParse.port(url))))
				print(req)

				#Send the http request data

				sock.sendall(req.encode())
				print(socket_full(sock))
		except IndexError:
			print("Enter a proper url\n")
		except socket.gaierror:
			print("Not a valid Domain\n")
		except:
			raise

#Start cmd loop

try:
	Terminal().cmdloop()

#Raise keyboard interrupt as a exit

except KeyboardInterrupt:
	print('\n\nKeyboard Interrupt Detected. Exiting...\n\n')

#Raise all other errors that appear

except:
	raise
