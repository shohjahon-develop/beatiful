from django.urls import path
from .views import index,about,client,contact, products


urlpatterns=[
  path('index/',index ,name="index"),
  path('about/',about ,name="about"),
  path('client/',client,name="client"),
  path('products/',products,name="products"),
  path('contact/',contact,name="contact"),
]