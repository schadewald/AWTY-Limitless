from flask_pymongo import pymongo


client = pymongo.MongoClient(
    "mongodb+srv://AWTY:Limitless@cluster0.zodbm.mongodb.net/Limitless?retryWrites=true&w=majority")
db = client.get_database('Limitless')
NBA = pymongo.collection.Collection(db, 'NBA')
