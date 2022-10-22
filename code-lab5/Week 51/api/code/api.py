from random import randint
from flask import Flask, jsonify
import json
import os
#import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

def get_conn():
    db_name = os.environ.get('DB_NAME')
    db_user = os.environ.get('PG_USER')
    db_pass = os.environ.get('PG_PASS')
    db_host = os.environ.get('DB_HOST')
    db_port = os.environ.get('PG_PORT')

    conn_string = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
    db_con = create_engine(conn_string)
    return db_con

def get_meal_reco():
    db = get_conn()
    query ="SELECT MealName, MealPrice FROM Meals ORDER BY RANDOM() LIMIT 1;"
    reco = db.execute(query)
    reco_l = []
    #reco_l = {}
    print("reco is", reco)
    for r in reco:
        print("r is", r)
        p = (r[0], r[1])
        reco_l.append(p)
    return list(reco_l)

@app.route('/')
@app.route('/recommendation/')
def index():
    return jsonify(get_meal_reco())

app.run(host='0.0.0.0', port=os.environ.get('API_PORT'))