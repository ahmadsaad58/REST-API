from flask import Flask, g
from flask_restful import Resource, Api, reqparse
import os
import markdown
import shelve

# create an instance of Flask 
app = Flask(__name__) 

# create the API
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Presents the api docs at homepage
@app.route("/")
def index(): 
	# present documentation 

	# open the README
	with open(os.path.dirname(app.root_path) + '/README.md', "r") as file:
		content = file.read()
		# convert to HTML
		return markdown.markdown(content)


class DeviceList(Resource):
	def get(self):
		shelf = get_db()
		keys = list(shelf.keys())

		devices = []

		for key in keys:
			devices.append(shelf[key])

		return {'message': 'Success', 'data': devices}, 200