from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import ConnectionFailure

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    #Added username and password variables to the __init__ so class can be instantiated for a specific username, password and port when called rather than hard coding them.
    #Did the same for port and databaseName to generalize the class as little further and maximize its re-usability.
    def __init__(self, port, databaseName, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:{}/{}'.format(port, databaseName) % (username, password))

        #Testing and troubleshooting.
        try:
            self.client.admin.command('ping')
        except ConnectionFailure:
            print("connection failed")

        self.database = self.client[databaseName]
        collections = self.database.list_collection_names()
        #print(collections)

    #Complete this create method to implement the C in CRUD.
    #Implement this to let the user change the collection name, which seemed useful with the init change to let this be used with other databases.
    #For purposes of module 4 collection needs to be animals.
    def create(self, collection, data):
        if data is not None:
            #returns True if successful insert of data and False if unsuccessful.
            # data should be dictionary
            result = self.database[collection].insert(data)
            if result is not None:
                print(result)
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        return False

# Create method to implement the R in CRUD.
    #collection is the collection to perform the query on, key and value are the key and value pair to use in the search.
    def readQuery(self, collection, query):
        result = self.database[collection].find(query, {"_id":0})
        if result.count() > 0:
            return result
        else:
            raise Exception("No data returned from query")            

# Create method to implement the R in CRUD.
    # collection is the collection to perform the query on, key and value are the key and value pair to use in the search.
    def readOne(self, collection, key, value):
        query = {key: value}
        result = self.database[collection].find(query)
        if result.count() > 0:
            return result
        else:
            raise Exception("No data returned from query")            

    #Method to implement the U in CRUD.
    def update(self, collection, key, value, data):
        query = {key: value}
        result = self.database[collection].update(query, data)
        if result is not None:
            return result
        else:
            raise Exception("No data returned from update")

    #Method to implement the D in CRUD.
    # collection is the collection to perform the query on, key and value are the key and value pair to use in the search.
    def delete(self, collection, key, value):
        query = {key: value}
        result = self.database[collection].remove(query)
        if result is not None:
            return result
        else:
            raise Exception("No returned result from document deletion")
