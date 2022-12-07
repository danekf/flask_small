# allows any view to access mongoDb

from pymongo import MongoClient

#import dotenv and load
import os
import sys
import dotenv
dotenv.read_dotenv()

#set variables from env
DB_CONNECTION_STRING = str(os.environ.get('DB_CONNECTION_STRING'))
 # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
client = MongoClient(DB_CONNECTION_STRING)

def db_message():
   message = 'temp (hello)'
   return message


def get_database(db_name):  
   # Create/get the database with the given name when calling it
   return client[db_name]


def insert_name(db_name, name):   
   #define db
   db = client[db_name]
   
   #define collection in db to insert to
   col = db['users']
   
   #define entry itself
   entry = {'name': name}
   
   #insert one entry into defined column, use insert_many for many entries in an array
   col.insert_one(entry)
   
   
def get_data():
   #get data from sample
   db = client['sample_mflix']
   #collection is comments
   col = db['comments']
   #get first entry
   x = col.find_one()
   
   return(x)
   
   
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()