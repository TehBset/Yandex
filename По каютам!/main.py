from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/distribution')
def training():
    lists = ['Jackson', 'Jack', 'Son', 'Ackson']
    return render_template('base.html', lists=lists)


if __name__ == '__main__':
    app.run(port=8070, host='127.0.0.1')
