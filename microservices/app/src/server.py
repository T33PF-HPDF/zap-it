from src import app
from flask import request
from flask_restful import Resource, Api
from requests import post
from json import dumps

api = Api(app)

class CreateRow(Resource):
    def get(self):
        return {'Parameters':'id,name,created_on,modified_on,desc in JSON format','Desc':'Creates a row in a Google spreadsheet.'}
    def put(self):
##        row = {
##            'id': request.form['id']
##            ,'name': request.form['name']
##            ,'created_on': request.form['created_on']
##            ,'modified_on': request.form['modified_on']
##            ,'desc': request.form['desc']}
##        url = 'https://hooks.zapier.com/hooks/catch/2836701/8fmhzu/'
##        response = post(
##            url=url, json=dumps(row))
        return request.form['desc']

api.add_resource(CreateRow, '/CreateRow')
    
