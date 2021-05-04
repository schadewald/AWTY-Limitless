from flask_pymongo import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://<ORGANIZATION>:<PASSWORD>@cluster0.zodbm.mongodb.net/<COLLECTION>?retryWrites=true&w=majority")
db = client.get_database('<COLLECTION>')
NBA = pymongo.collection.Collection(db, 'NBA')
Schedule = pymongo.collection.Collection(db, 'Schedule')
ELO = pymongo.collection.Collection(db, 'ELO')
Results = pymongo.collection.Collection(db, 'Results')
