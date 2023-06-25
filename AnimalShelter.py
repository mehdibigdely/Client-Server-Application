# Example Python Code to Insert a Document
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'snhu4321'
        HOST = 'localhost'
        PORT = 27017
        DB = 'AACTest2'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            #print ("Successfully inserted ") 
            #print (data)
            return True
        else:
            #print ("Data non")
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        
# Create method to implement the R in CRUD.
    def read(self, parametrer='{}'):
     # if data value is not None or empty, it is passed to find method and will return all rows which matches the data criteria
        data = self.database.animals.find(parametrer)
        return data

# Create method to implement the R in CRUD * only reads one.
    def read_one(self, parametrer):
        # if data value is not None or empty, it is passed to find method and will return all rows which matches the data criteria
        data = self.database.animals.find_one(parametrer)
        return data


# Method to implement the U in CRUD => update method
    def update(self, filter_data, update):
        # if data value is not None or empty, it is passed to find method and will return all rows which matches the data criteria

        if filter_data is None:
            # if there is no filter or update criteria then all the rows will be return
            raise Exception("Nothing to update, because data or update parameter is empty")
        else:
            data = self.database.animals.update_one(filter_data, update)
            return True


# Method to implement the D in CRUD => delete method
    def delete(self, delete):
        # if data value is not None or empty, it is passed to find method and will return all rows which matches the data criteria
        status = False
        if delete is None:
            # if there is no filter or update criteria then all the rows will be return
            raise Exception("Nothing to delete, because data parameter is empty")
        else:
            # counter to return the number of documents to be deleted
            count = 0
            # iterates array dictionary and deletes the documents based on the given key and value 
            for i in delete:
                data = self.database.animals.delete_one(i)
                count += 1
            status = True
        return count
