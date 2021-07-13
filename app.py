from flask import Flask
from flask import json

import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s , %(message)s', level=logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )

    logging.debug('/status was reached.')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

    logging.debug('/metrics was reached.')
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
