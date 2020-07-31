import re

class HTTPParse:
	#Create a dictionary to check for native ports
	global default_ports
	default_ports = {'https':443, 'http':80, 'ftp':21}
	#Parse Host
	def host(url):
		'''Prepare domain'''
		return(re.split(r"\:", (re.split(r"\/", url))[2])[0])
	#Parse Port Number
	def port(url):
		'''Try to select port'''
		if (re.split(r"\:", url).__len__() > 2):
			return((re.search(r"\d+", (re.split(r"\:", url))[2]))[0])
		for key, value in default_ports.items():
			if url.startswith(key):
				return(value)
	#Parse FilePath
	def filepath(url):
		'''Try to select path'''
		files = re.split(HTTPParse.host(url), url)[-1]
		if re.search(r"^\:", files):
			files = re.split(r"^\:\d+", files)[-1]
		if not re.search(r"^\/", files):
			files = "/" + files
		return(files)
