import os
from io import StringIO

import flask
import pandas as pd
from flask import Flask, request
import prophet_script

ALLOWED_EXTENSIONS = {'txt', 'xlsx', 'csv'}

app = Flask(__name__)
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def asdf():
     return "Dupa"

@app.route("/predict", methods=['POST'])
def connecttomodel():

     if 'file' not in request.files:
          return 'No file part in the request', 400
     file = request.files['file']

     if file.filename == '':
          return 'No file selected for uploading', 400

     model = request.args.get('model')
     try:
          country = request.args.get('country')
          industry = request.args.get('industry')
          isRetail = False if request.args.get('isRetail') == '0' else True
          period = 30 if request.args.get('period') == None else int(request.args.get('period'))
          freq = 'D' if request.args.get('frequency') == None else request.args.get('frequency')

          df = pd.read_csv(StringIO(file), sep=";")
          data = prophet_script.useProphet(country, industry, isRetail, period, freq, df)
          # rm file?

          if data == 1:
               return "Processing failed", 400
          response = flask.jsonify(data)
          response.headers.add('Access-Control-Allow-Origin', '*')
          return response

     except:
          return ['Incorrect parameters', 400]

@app.route("/predict", methods=['GET'])
def localconnecttomodel():

     model = request.args.get('model')
     try:
          country = request.args.get('country')
          industry = request.args.get('industry')
          isRetail = False if request.args.get('isRetail') == '0' else True
          period = 30 if request.args.get('period') == None else int(request.args.get('period'))
          freq = 'D' if request.args.get('frequency') == None else request.args.get('frequency')
          filename = "Chemia.csv" if request.args.get('filename') == None else request.args.get('filename')
          df = pd.read_csv(filename)
          data = prophet_script.useProphet(country, industry, isRetail, period, freq, df)
          # rm file?


          if data == 1:
               return "Processing failed", 400
          return data
     except:
          return ['Incorrect parameters', 400]

if __name__ == '__main__':
     app.run(debug=True, host="0.0.0.0")
