################################# Import Libraries ###################################################
import os.path
from bottle import route, run, response, static_file, request, error, Bottle, template
from json import dumps, loads, load
from collections import OrderedDict
#################################### WebService Route / ##############################################
class API:
	def __init__(self, port, local):
		self._app = Bottle()
		self._route() # During initialisation we launch the _route() method to register the routes enabled

		self._local = local
		self._port = port

		if local:
			self._host = '127.0.0.1'
		else:
			self._host = '0.0.0.0'

	def start(self):
		self._app.run(server='paste', host=self._host, port=self._port)

	def _route(self):
		self._app.hook('before_request')(self._strip_path) # Needed to prevent errors.
		self._app.route('/', callback=self._homepage) # We tell to the API to listen on "/" and execute the restapionmark  "_homepage()" when "/" is called

		# We tell the API to execute _doAction() when a POST Request is perform on "/restapionmark"
		self._app.route('/action', method="POST", callback=self._doAction)

		# We tell the API to execute _doAction() when a GET Request is perform on "/restapionmark"
		self._app.route('/restapionmark', method="GET", callback=self._doGetMark)

	def _strip_path(self):
		request.environ['PATH_INFO'] = request.environ['PATH_INFO'].rstrip('/')

	def _homepage(self):
		return static_file("index.html", root=os.getcwd()+'\\html') # We return the "index.html" file as a static file.

	def _doAction(self):
		rv = {"status": "Success"} # We create a dictionary with the key "status" = "success"
		response.content_type = 'application/json' # we set the correct "response.content_type" to "json" format, because "json" is nice and cool !

		return dumps(rv) # We dump the dictionary into json file and return it.
	def _doGetMark(self):
 
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

		#print(json.dumps(my_dictionary))
		rv = my_attributes
		#rv = {"status": "Employed", "Mark": "knows RESTful API", "} # We create a dictionary with the key "status" = "success"
		#rv = {"status": "Employed", "Mark": "knows RESTful API", "} # We create a dictionary with the key "status" = "success"
		response.content_type = 'application/json' # we set the correct "response.content_type" to "json" format, because "json" is nice and cool !

		return dumps(rv, indent=4) # We dump the dictionary into json file and return it.
