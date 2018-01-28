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
            content = request.data
            content = content.decode(encoding='UTF-8')
##            parser = reqparse.RequestParser()
##            parser.add_argument('data', type=str, help='Test string')
##            args = parser.parse_args(strict=True)
            if content['id'] == '1236':
                return 'Victory is ours!'
            
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
    
