# allows any view to access mongoDb

from pymongo import MongoClient

#import dotenv and load
import os
import sys
import dotenv
dotenv.read_dotenv()

#set variables from env
DB_CONNECTION_STRING = str(os.environ.get('DB_CONNECTION_STRING'))

def utils_message():
   print('hello')


def get_database(): 
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = DB_CONNECTION_STRING
   
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database
   return client['user_shopping_list']
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()