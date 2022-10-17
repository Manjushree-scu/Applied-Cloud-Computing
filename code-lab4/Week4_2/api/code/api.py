from random import random
from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

menu = [{'AVOCADO JHALMURI':'$10.00'},
        {'SPECIAL SAMOSA':'$9.00'},
        {'TANDOORI VEGETABLE':'$20.00'},
        {'ACHARI CHICKEN TIKKA':'$21.00'},
        {'TOMATO AND FENNEL SOUP':'$10.00'},
        {'MULLIGATAWANY SOUP':'$10.00'},
        {'BOMBAY FISH MASALA':'$22.00'},
        {'YELLOW DAL TARKA':'$19.00'},
        {'KADHAI BHINDI':'$20.00'},
        {'GARDEN PIZZA':'$23.00'},
        {'PEPPERONI PIZZA':'$25.00'},
        {'GARLIC BREAD':'$8.00'},
        {'CALZONE':'$15.00'},
        {'PANINI':'$15.00'},
        {'SALAD':'$5.00'}]

os.environ["API_ENDPOINT"]='meal'

api_endpoint = os.environ.get("API_ENDPOINT")
@app.route('/')
def get_reco():
    choice = random.randint(0,14)
    return jsonify(menu[choice])

if __name__ == '__main__':
    port = os.environ.get('API_PORT',5000)
    app.run(host='0.0.0.0',port=port)