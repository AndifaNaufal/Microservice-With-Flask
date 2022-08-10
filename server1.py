from flask import Flask,jsonify
import requests
app = Flask(__name__)


@app.route('/tasks', methods=['GET'])
def get_tasks():
    url = 'http://universities.hipolabs.com/search?country=United+States'
    headers = {}
    response = requests.request('GET',url)
    #print(response.text)
    return response.text

@app.route('/')
def index():
    return "Hello, cloud!"

if __name__ == '__main__':
    app.run(debug=True,port=5001)