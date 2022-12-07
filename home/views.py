from django.shortcuts import render
from django.http import HttpResponse

from folio.utils import utils_message


# Create your views here.

def index(req):
  #render index.html as main home page
  message = utils_message()
  
  context = {
    'message': message
  }
  
  return render(req,
                'index.html', context)  
  