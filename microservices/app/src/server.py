from src import app
from flask import request
from flask_restful import Resource, Api, reqparse
from requests import post
from json import dumps

api = Api(app)

class CreateRow(Resource):
    def get(self):
        return {'Parameters':'id,name,created_on,modified_on,desc all in a dictionary','Desc':'Creates a row in a Google spreadsheet.'}
    def put(self):
        if request.method == "PUT":
            return request.data.decode(encoding="UTF-8")
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str, help='ID')
            parser.add_argument('name', type=str, help='Name')
            parser.add_argument('created_on', type=str, help='Created on')
            parser.add_argument('modified_on', type=str, help='Last Modified on')
            parser.add_argument('desc', type=str, help='Description')
            args = parser.parse_args()
            
            return args
            
            if request.form.get('id',"None") != "None":
                row = {
                    'id': request.form['id']
                    ,'name': request.form['name']
                    ,'created_on': request.form['created_on']
                    ,'modified_on': request.form['modified_on']
                    ,'desc': request.form['desc']}
                url = 'https://hooks.zapier.com/hooks/catch/2836701/8fmhzu/'
                response = post(
                    url=url, json=dumps(row))
                return response.text
            else:
                return args
        else:
            return "Bad Request: Not a PUT request"

api.add_resource(CreateRow, '/CreateRow')
    
