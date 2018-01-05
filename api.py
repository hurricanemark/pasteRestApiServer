################################# Import Libraries ###################################################
import os.path
from bottle import route, run, response, static_file, request, error, Bottle, template
from json import dumps, loads, load
from collections import OrderedDict
#################################### WebService Route / ##############################################
class API:
	def __init__(self, port, local):
		# During initialization, launch the _route() method to register the routes enabled
		self._app = Bottle()
		self._route()

		self._local = local
		self._port = port

		if local:
			self._host = '127.0.0.1'
		else:
			self._host = '0.0.0.0'

	def start(self):
		self._app.run(server='paste', host=self._host, port=self._port)

	def _route(self):
		# _app.hook is needed to prevent errors.
		self._app.hook('before_request')(self._strip_path) 

		# Tell the API to listen on "/" and execute the restapionmark  "_homepage()" when "/" is called
		self._app.route('/', callback=self._homepage) 

		# Tell the API to execute _doAction() when a POST Request is perform on "/action"
                # e.g. http://127.0.0.1:7777/action
		self._app.route('/action', method="POST", callback=self._doAction)

		# Tell the API to execute _doGetMark() when a GET Request is perform on "/restapionmark"
                # e.g. http://127.0.0.1:7777/restapionmark
		# note that your external ipaddress should work here too.
		self._app.route('/restapionmark', method="GET", callback=self._doGetMark)

	def _strip_path(self):
		request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')

	def _homepage(self):
		return static_file("index.html", root=os.getcwd()+'\\html') # We return the "index.html" file as a static file.

	def _doAction(self):
		# service the landing page with json reponse
		# Create a dictionary with the key "status" = "success" 
		rv = {"status": "Success"} 
		# Set the correct "response.content_type" to "json" format
		response.content_type = 'application/json' 

		return dumps(rv) # We dump the dictionary into json file and return it.
	def _doGetMark(self):
		# for simplicity, a static dictionary.  
		# in real world practices, it should come from dynamic source such as SQL querry, load file, etc.
		my_attributes = OrderedDict ({
			"Name": "Mark V. Nguyen",
			"Current position": "Principal software engineer",
			"Current role": "CTO",
			"School": ["CalPoly, SLO --B.S. Computer Engineering --1996", "Monterey High School --1989"],
			"Employable": True,
			"Experience": {
			"Favorite": "RESTful API in Python",
			"Languages": 'C, C#, Python, Java, JavaScript',
			"Key skills": 'Multithreading, Containerization, Configuration management'
			},
			"Sites": ['https://www.linkedin.com/in/marknltv','https://hub.docker.com/u/marknre', 'https://github.com/markwhackadoo', 'http://aesclever.com/aftp/.tmp2011/MarkResume2017.pdf'],
			"Work history": {
			"2001-Present": "Applied Expert Systems Inc.",
			"2000-2001": "SS8 Inc.",
			"1997-2000": "SBE Inc.",
			"1996-1997": "Microsoft Corp."
			}
		})

		#print(json.dumps(my_attributes))
		rv = my_attributes
		# set the correct "response.content_type" to JSON format
		response.content_type = 'application/json' 
		# return the dictionary using json.dumps 
		return dumps(rv, indent=4) 
