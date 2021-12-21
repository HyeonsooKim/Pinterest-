from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

#편하게 사용하기 위해 만드는 변수
app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accountapp/logout.html'), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
]