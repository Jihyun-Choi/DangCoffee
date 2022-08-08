from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'LogInOutApp'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='LogInOutApp/login.html'), name='login'),
]