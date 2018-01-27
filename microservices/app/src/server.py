from src import app
from flask import jsonify,request,make_response,url_for,redirect
import requests,json

# Set the webhook_url to the one provided by Zapier when you create the webhook
globalCreateRowWebhook = 'https://hooks.zapier.com/hooks/catch/2836701/8fmhzu/'

@app.route("/")
def home():
    return "ZapIt : Backend! - Hello Global User"

@app.route('/create-row-in-gs', methods=['GET','POST'])
def create_row_in_gs():
    return str(request.method+" "+request.json['t_name'])
##    if request.method == 'GET':
##        return make_response('Failure')
##    if request.method == 'POST':
##        t_id = request.json['id']
##        t_name = request.json['name']
##        created_on = request.json['created_on']
##        modified_on = request.json['modified_on']
##        desc = request.json['desc']
##        
##        create_row_data = {'id': str(t_id),'name':str(t_name),'created-on':str(created_on),'modified-on':str(modified_on),'desc':str(desc)}
##        
####        response = requests.post(
####            globalCreateRowWebhook, json=json.dumps(create_row_data),
####            headers={'Content-Type': 'application/json'})
##        return response.content
    
