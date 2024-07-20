from django.urls import path
from . import views  

urlpatterns = [
    path('', views.wine_tasting, name='wine_tasting'),  
   
]