from flask import Flask, jsonify
import requests
app = Flask(__name__)

@app.route('/getdataserver1',methods=['GET'])
def get_tasks1():
    url = 'http://localhost:5001/tasks'
    headers = {}
    response = requests.request('GET',url)
    #print(response.text)
    return response.text

@app.route('/getdataserver2',methods=['GET'])
def get_data():
    url = 'http://localhost:5002/get_data'
    headers = {}
    response = requests.request('GET',url)
    #print(response.text)
    return response.text

@app.route('/')
def index():
    return "Hello, Ini serverGateWay!"

if __name__ == '__main__':
    app.run(debug=True,port=5000)