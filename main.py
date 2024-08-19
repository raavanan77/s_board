from flask import Flask, request,render_template,jsonify
from database import dbess
import jinja2
from dotenv import load_dotenv
import os

load_dotenv()

env = jinja2.Environment()
env.globals.update(zip=zip)

db_handler = dbess(os.getenv('DBCONSTR'))

maindb = ''

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    options = db_handler.listdb()
    return render_template('home.html', dblist=options, collection=[])


@app.route('/update-collections', methods=['POST'])
def handle_option():
    global maindb
    # Get the selected option from the POST request
    maindb = request.json.get('option')
    # Call the function based on the selected option
    collections = db_handler.selcollection(maindb)

    return jsonify({'collections': collections})

@app.route('/submit', methods=['POST'])
def submit():
    global maindb
    # This function is called when the form is submitted
    user_input = request.form['options']
    options = db_handler.get_data(dbname=maindb,collectionname=user_input)  # Call the function to process the input
    print(options['_id'])
    return render_template('result.html',result=options['_id'])

if __name__ == '__main__':
    app.run(debug=True)