#! /usr/bin/env python3

from flask import Flask
from flask import jsonify
import dogs_fact


app = Flask(__name__)

@app.route('/')
def index():
    fact = dogs_fact.get_fact()
    return jsonify(fact), 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

