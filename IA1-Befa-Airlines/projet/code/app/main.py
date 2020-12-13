from flask import Flask
from flask import render_template
from flask import request
import xml.etree.ElementTree as ET

app = Flask(__name__)


@app.route('/buy/')
def buy():
    return render_template('index.html')


@app.route('/buy/', methods=['POST'])
def login():
    if request.method == 'POST':
        tmp = request.form['code']
        code = tmp.replace(" ", "")
        # for elem in root:
        #    for e in elem:
        #       if code in
        return tmp
    else:
        return "GET Request not authorized"


tree = ET.parse('items.xml')
root = tree.getroot()

if __name__ == "__main__":
    app.run()
