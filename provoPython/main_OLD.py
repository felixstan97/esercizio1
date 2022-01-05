try:
    # Python 3
    from http.server import HTTPServer, SimpleHTTPRequestHandler, test as test_orig
    import sys
    from flask import Flask, jsonify
    import requests 
    import json

    resto = {'uno': 2,'tre': 'quattro'}
    qui= 'hola'

    app = Flask(__name__)

    @app.route('/')
    def index():
        res = '{"uno": "due","tre": "quattro"}'
            
        return qui
        
        
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

    def test (*args):
        test_orig(*args, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
except ImportError: # Python 2
    from BaseHTTPServer import HTTPServer, test
    from SimpleHTTPServer import SimpleHTTPRequestHandler

class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        SimpleHTTPRequestHandler.end_headers(self)

if __name__ == '__main__':
    test(CORSRequestHandler, HTTPServer)