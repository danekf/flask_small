from django.shortcuts import render
from django.http import HttpResponse

import folio.db as db


# Create your views here.

def index(req):
  #render index.html as main home page
  message = db.db_message()
  
  # get test database
  entry = db.get_data()
  
  
  
  context = {
    'message': message,
    'entry': entry
  }
  
  return render(req,
                'index.html', context)  
  