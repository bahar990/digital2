from django.urls import path
from digital.views import Productlist


urlpatterns = [
    path('',Productlist.as_view()),
    

]