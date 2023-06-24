from django.urls import path
from .views import *

urlpatterns = [
    path('register/', register , name='register'),
    path('login/', login_page , name='login'),
    path('', home , name='home'),
    path('logout/', logout_page , name='logout'),
]