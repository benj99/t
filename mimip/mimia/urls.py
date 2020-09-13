from django.urls import path
from . import views

app_name = 'mimia'

urlpatterns = [
    path('',views.home,name='home')
]
