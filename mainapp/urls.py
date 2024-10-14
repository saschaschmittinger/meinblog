from django.urls import path
from .views import *

urlpatterns =[
    path('',BlogContent_view.as_view() , name='home_view')
]