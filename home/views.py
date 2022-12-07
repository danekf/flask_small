from django.shortcuts import render
from django.http import HttpResponse

from folio.db import db


# Create your views here.

def index(req):
  #render index.html as main home page
  message = db_message()
  
  db.get_database()
  
  context = {
    'message': message
  }
  
  return render(req,
                'index.html', context)  
  