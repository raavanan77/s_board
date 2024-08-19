import requests
import pymongo




class dbess:



    def __init__(self,connectionstring):
        self.dbconnection = pymongo.MongoClient(connectionstring)

        self.dbclose = lambda: self.dbconnection.close()

    #update_one({'_id': "verify"},{"$set": {"ver":ctx.channel.id,"vermsgid":msg.id}}, upsert=True)
    def listdb(self):
        return self.dbconnection.list_database_names()

    def selectdb(self, dbname):
        return self.dbconnection[dbname]

    def selcollection(self,dbname):
        db = self.dbconnection[dbname]
        return db.list_collection_names()

    def createdb(self,dbname):
        create = self.dbconnection()
        newdb = create[dbname]
        self.dbclose
        return newdb
    
    def get_data(self,dbname,collectionname):
        maindb = self.selectdb(dbname)
        collection = maindb[collectionname]
        return collection.find_one()
