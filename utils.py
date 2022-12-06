# allows any view to access mongoDb

#from pymongo import MongoClient

import os
import sys
import dotenv

dotenv.read_dotenv()
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_DB_PASSWORD')
print(DB_USERNAME, DB_PASSWORD)




# def get_database():
  
 
#    # Provide the mongodb atlas url to connect python to mongodb using pymongo
#    CONNECTION_STRING = "mongodb+srv://" + DB_USERNAME + ":" + DB_PASSWORD + "@sharedcluster.g2v2uvl.mongodb.net/?retryWrites=true&w=majority"
   
 
#    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#    client = MongoClient(CONNECTION_STRING)
 
#    # Create the database for our example (we will use the same database throughout the tutorial
#    return client['user_shopping_list']
  
# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":   
  
#    # Get the database
#    dbname = get_database()