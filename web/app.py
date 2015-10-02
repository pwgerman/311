from flask import Flask, render_template
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
    app.run()
