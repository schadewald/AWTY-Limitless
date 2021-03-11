from flask import Flask, jsonify, request
import db
import json

app = Flask(__name__)


# test server
@app.route('/')
def test():
    return "Database server is running!"


# test to insert sample data to the data base
@app.route('/db/update/test')
def update_db_test():
    with open('sampleData.json') as file:
        file_data = json.load(file)
    db.db.NBA.insert(file_data)
    return "Updated the data base with test data!"


# insert JSON data to the data base
# curl --header "Content-Type: application/json" --request POST --data @./sampleData.json http://127.0.0.1:4321/db/update
# above command will send a local JSON file
@app.route('/db/update', methods=['POST'])
def update_db():
    data = request.get_json()
    #below clears db before new data / this needs to be removed when not in development
    #db.db.NBA.remove({})
    db.db.NBA.insert(data)
    return "Data Base Updated"


# this can be used each time the database is reset with up to date stats
@app.route('/db/clear')
def clear_db():
    db.db.NBA.remove({})
    return "DB is now empty, and ready for the next day!"


# get current stats
@app.route('/db/retrieve')
def retrieve_db():
    query = db.db.NBA.find()
    output = {}
    i = 0
    for x in query:
        output[i] = x
        output[i].pop('_id')
        i += 1
    return jsonify(output)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4321)
