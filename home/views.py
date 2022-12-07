from django.shortcuts import render
from django.http import HttpResponse

import folio.db as db


# Create your views here.

def index(req):
  #render index.html as main home page
  message = db.db_message()
  
  # get sample database
  entry = db.get_data('sample_mflix', 'comments')
  
  #insert into test database
  insert = db.insert_into('testDb', 'folio', 'Danek')
  
  context = {
    'message': message,
    'entry': entry,
    'insert': insert
  }
  
  return render(req,
                'index.html',  
                context)  
  