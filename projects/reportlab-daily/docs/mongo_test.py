import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client['charge']
bid = db.bid


def count():
    number = bid.count()
    print number


def query(field):
    biddata = bid.find({}, {"_id": 0})
    for doc in biddata:
        print doc[field]

count()
query("cid")
