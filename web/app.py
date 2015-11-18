from flask import Flask, render_template, jsonify, request
from pandas import to_datetime

from lib.ml311 import predict
import util.template_filters as filters
import requests

API_URL = "https://data.sfgov.org/resource/vw6y-z8j6.json"
app = Flask(__name__)
app.jinja_env.filters['datetime'] = filters.datetime
app.jinja_env.filters['timedelta'] = filters.timedelta


@app.route('/')
def root():
    return render_template('index.html');

@app.route('/about')
def about():
    return render_template('about.html');

@app.route('/insights')
def get_insight():
    return render_template('insights.html');

@app.route('/ticket')
def get_ticket():
    case_id = request.args.get('case_id')
    res = requests.get(API_URL, params={'case_id': case_id})
    if res.status_code < 300:
        response_data = res.json()
        if not response_data:
            return render_template("ticket.html", case_id=case_id)

        ticket = response_data[0]
        prediction = predict(ticket['opened'])
        closed = {}
        if 'closed' in ticket:
            closed_date = to_datetime(ticket['closed'])
            difference = closed_date - prediction
            which = difference.days > 0
            which = 'longer' if which else 'shorter'
            time_open = to_datetime(ticket['opened']) - closed_date
            closed = {
                'date': closed_date,
                'time_open': time_open,
                'difference': difference,
                'which': which
            }
        else:
            closed = None

        return render_template("ticket.html",
                               prediction=prediction,
                               closed=closed)

if __name__ == '__main__':
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


