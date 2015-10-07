from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html');

@app.route('/ticket/<ticket>')
def get_ticket(ticket):
    return {
        'im a': 'ticket'
    }

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
