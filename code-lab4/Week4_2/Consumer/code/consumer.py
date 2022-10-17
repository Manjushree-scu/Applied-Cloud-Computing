import requests
from flask import Flask, render_template
from flask import request
import os

app = Flask(__name__)

host=os.environ.get('API_HOST',"api.")
api_port=os.environ.get('API_PORT',5000)

api_url="http://"+host+".:"+api_port+"/"

@app.route('/')
def get_reco():
    rcvd =requests.get("http://api.:5000/")
    f_item = rcvd.text
    return render_template('webpage.html',food=f_item)
    
if __name__ == '__main__':
    port = os.environ.get('CONSUMER_PORT',80)
    app.run(host='0.0.0.0',port=port)