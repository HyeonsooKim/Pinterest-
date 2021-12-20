from django.urls import path

from accountapp.views import hello_world

#편하게 사용하기 위해 만드는 변수
app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]