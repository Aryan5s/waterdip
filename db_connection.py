import pymongo 

# mongodb://localhost:27017
# mongodb+srv://as3mh5:<password>@cluster0.st8tcvb.mongodb.net/

url = 'mongodb+srv://as3mh5:cVLyTKl08ZlCl1LE@cluster0.st8tcvb.mongodb.net/'
client = pymongo.MongoClient(url)
db = client['waterdip']