import flask
from flask import json
from flask import render_template
from flask import request

from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    template_params = {
        'foo': 'bar',
        'blah': 'blah'
    }
    # ** is used to convert the dictionary into key value pairs
    # return render_template('index.html', **template_params)

    # return render_template('manage/index.html', foo=bar, blah=blah)
    return json.jsonify({'foo': 'bar'})

# This is just for debug mode so you don't have to run Apache
if __name__ == '__main__':
    app.debug = True
    app.run()

