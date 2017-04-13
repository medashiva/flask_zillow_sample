#!/usr/bin/python
import os
from flask import Flask, render_template, request
from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults

app = Flask(__name__)


@app.route('/')
def index():
    address = '1305 Middlefield Rd, Palo Alto'
    zipcode = '94301'
    zillow_data = ZillowWrapper('xxxxx')
    deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
    print deep_search_response
    result = GetDeepSearchResults(deep_search_response)
    print result.zestimate_amount
    return "hello"



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
