from flask import Flask, render_template, jsonify, request

from lib.ml311 import predict
import requests

API_URL = "https://data.sfgov.org/resource/vw6y-z8j6.json"
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html');

@app.route('/ticket')
def get_ticket():
    case_id = request.args.get('case_id')
    res = requests.get(API_URL, params={'case_id': case_id})
    if res.status_code < 300:
        response_data = res.json()
        prediction = predict(response_data[0]['opened'])
        return render_template("ticket.html", completion_date=prediction)

if __name__ == '__main__':
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


