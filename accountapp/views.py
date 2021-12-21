from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World!')
    # return HttpResponse('안녕하세요 !')
    if request.method == "POST":
        #request에 POST 메서드에서 hello_world_input이라는 데이터를 가져와라
        temp = request.POST.get('hello_world_input')

        #HelloWorld라는 객체
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        #db에 저장
        new_hello_world.save()

        #HelloWorld의 모든 오브젝트를 담는다
        hello_world_list = HelloWorld.objects.all()
        #redirect는 재접속하라, reverse는 accountapp:hello_world에 해당하는 경로를 다시 만들어주는 것
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'