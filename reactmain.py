from flask import Flask, jsonify, request
from flask_cors import CORS
from database import dbess
import jinja2
from dotenv import load_dotenv
import os

load_dotenv()

env = jinja2.Environment()
env.globals.update(zip=zip)

db_handler = dbess(os.getenv('DBCONSTR'))

app = Flask(__name__)
CORS(app)  # This will allow CORS for all domains

@app.route('/api/databaselist', methods=['GET'])
def get_databaselist():
    global db_handler
    data = jsonify(db_handler.listdb())
    print(data)
    return data

@app.route('/api/echo', methods=['POST'])
def echo():
    data = request.json
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
