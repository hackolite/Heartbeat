from flask import Flask
from flask import request
from QRSDetectorOnline import QRSDetectorOnline
app = Flask(__name__)
qrs = QRSDetectorOnline()


@app.route('/import', methods = ['GET', 'POST', 'DELETE'])
def user():
    if request.method == 'POST':
        """modify/update the information for <user_id>"""
        # you can use <user_id>, which is a str but could
        # changed to be int or whatever you want, along
        # with your lxml knowledge to make the required
        # changes
        data = request.form # a multidict containing POST data
        #print(request.get_data().decode('ascii'))
        try:
            qrs.process_measurement(request.get_data())
        except Exception as e:
            print(e)

        return ''


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
