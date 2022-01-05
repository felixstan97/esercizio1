from flask import Flask, jsonify
import requests 
import json


resto = {'uno': 2,'tre': 'quattro'}
qui= 'hola'


app = Flask(__name__)

@app.route('/')
def index():
    res = {'uno': 4,'tre': 'quattro'}
    ris = jsonify(res)
    ris.headers.add("Access-Control-Allow-Origin", "*")
    return ris
    
    
@app.route("/je", methods=['GET'])
def get():

    return resto
    
@app.route("/jo", methods=['GET'])
def getJo():
    return jsonify(resto)
    
if __name__ == "__main__":
    app.run(debug=True)
''',host='0.0.0.0', port=4200'''

app.use(cors())
