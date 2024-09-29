from flask import Flask, request, send_file, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/request_file', methods=['POST'])
def request_file():
    file = request.files['fileToUpload']
    list_responses = []
    for line in file:
        param = line.decode('utf-8').strip()
        url = 'http://127.0.0.1:3030/respond'
        body = {'string' : param}
        response = requests.post(url, json=body)
        list_responses.append(response.json()['response'])
    return list_responses

@app.route('/request_session', methods=['POST'])
def request_session():
    url = 'http://127.0.0.1:3030/respond'
    body = {'string' : request.form['textInput']}
    response = requests.post(url, json=body)
    return response.json()['response']

if __name__ == '__main__':
    app.run(debug=True, port=4040)