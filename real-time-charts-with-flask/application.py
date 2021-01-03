#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __license__ = "MIT"
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
import json
import random
import time
from datetime import datetime
from flask import request
from flask import Flask, Response, render_template

application = Flask(__name__)
random.seed()  # Initialize the random number generator


global temp

@application.route('/')
def index():
    return render_template('index.html')

import json
@application.route('/chart-data')
def chart_data():
    def generate_random_data():
        global temp
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': temp})
            yield f"data:{json_data}\n\n"
            time.sleep(0.05)
    return Response(generate_random_data(), mimetype='text/event-stream')

@application.route('/import', methods = ['GET', 'POST', 'DELETE'])
def user():
    global temp
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        #ata = request.form # a multidict containing POST data
        #print(request.get_data().decode('ascii'))
        try:
            y = json.loads(request.get_data().decode('ascii'))
            for i in y["data"]:
                temp = i
            #temp = json.dumps(request.get_data().decode('ascii'))
        except Exception as e:
            print(e)

        return ''


if __name__ == '__main__':
    application.run(host="0.0.0.0", debug=True, threaded=True)
