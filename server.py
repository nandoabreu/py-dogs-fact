#! /usr/bin/env python3

from flask import Flask
from flask import request
from flask import jsonify
import platform
import dogs_fact


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    facts = 1
    if request.method == 'POST':
        facts = int(request.values.get("limit"))

    data = dogs_fact.get_fact(limit=facts)
    data['node'] = platform.node()
    return jsonify(data), 200


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

