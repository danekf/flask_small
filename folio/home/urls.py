#import path from django framework
from django.urls import path
#import views module, named this way just by convention
from . import views

urlpatterns = [
  #root path, and show index view
  path('', views.index)
]