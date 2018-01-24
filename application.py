from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')

def greeting():
    greeting = "hello bob"
    return render_template('Homepage.html', greeting=greeting)


if __name__ == '__main__':
    app.run()
