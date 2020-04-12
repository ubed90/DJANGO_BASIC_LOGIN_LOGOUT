from django.urls import path
from login_out import views


app_name = 'login_out'

urlpatterns = [
    path('register/' , views.register , name = 'register'),
    path('user_login/' , views.user_login , name = 'user_login'),
]
