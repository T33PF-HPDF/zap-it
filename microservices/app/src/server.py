from src import app
from flask import jsonify,request,make_response,url_for,redirect
from flask_restful import Resource, Api
import requests,json

api = Api(app)

class CreateRow(Resource):
    def get(self):
        return {'Parameters':'id,name,created_on,modified_on,desc in JSON format','Desc':'Creates a row in a Google spreadsheet.'}
    def put(self):
        row = {
            'id': request.form['id']
            ,'name': request.form['name']
            ,'created_on': request.form['created_on']
            ,'modified_on': request.form['modified_on']
            ,'desc': request.form['desc']}
        url = 'https://hooks.zapier.com/hooks/catch/2836701/8fmhzu/'
        response = post(
            url=url, json=dumps(row))
        return row

api.add_resource(CreateRow, '/CreateRow')
    
