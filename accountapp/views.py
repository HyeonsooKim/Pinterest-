from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


def hello_world(request):
    # return HttpResponse('Hello World!')
    # return HttpResponse('안녕하세요 !')

    if request.user.is_authenticated:
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
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))




class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    #template에서 사용하는 user객체의 이름을 다르게 설정해줄 수 있음
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

    def get(self, *args, **kwargs):
        #그대로임
        # return super().get(*args, **kwargs)
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        #그대로임
        # return super().get(*args, **kwargs)
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    def get(self, *args, **kwargs):
        # 그대로임
        # return super().get(*args, **kwargs)
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):
        # 그대로임
        # return super().get(*args, **kwargs)
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().post(*args, **kwargs)
        else:
            return HttpResponseForbidden()
