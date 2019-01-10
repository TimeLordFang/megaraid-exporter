#!/usr/bin/python
from flask import Flask
import megacli

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/metrics')
def metrics():
    result = megacli.main()
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9101)
