from flask import Flask, jsonify
import db
import json

app = Flask(__name__)


# test server
@app.route('/')
def test():
    return "flask mongodb atlas is running!"


# test to insert sample data to the data base
@app.route('/db/update')
def update_db():
    with open('sampleData.json') as file:
        file_data = json.load(file)
    db.db.NBA.insert(file_data)
    return "Connected to the data base!"


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
    app.run(port=4321)
