from src import app
from flask import jsonify
from json import dumps
from requests import post

globalCreateRowWebhook = 'https://hooks.zapier.com/hooks/catch/2836701/8fmhzu/'
globalCreateSpreadsheetWebhook = 'https://hooks.zapier.com/hooks/catch/2836701/8raumf/'
globalUpdateRowWebhook = 'https://hooks.zapier.com/hooks/catch/2836701/8v1s1s/'
globalDeleteRowWebhook = 'https://hooks.zapier.com/hooks/catch/2836701/8v1n8t/'

@app.route("/")
def home():
    return "ZapIt : Backend! - Hello Global User"

# Uncomment to add a new URL at /new

@app.route("/json")
def json_message():
    return jsonify(message="Hello Global User")

@app.route("/create-row-in-gs",methods=['POST'])
def create_row_in_gs():
    t_id = request.form['id']
    t_name = request.form['name']
    created_on = request.form['created_on']
    modified_on = request.form['modified_on']
    desc = request.form['desc']

    create_row_data = {'id': str(t_id),'name':str(t_name),'created-on':str(created_on),'modified-on':str(modified_on),'desc':str(desc)}

    response = requests.post(
        globalCreateRowWebhook, data=json.dumps(create_row_data),
        headers={'Content-Type': 'application/json'}
    )
    print(response)
    
    
    
    
