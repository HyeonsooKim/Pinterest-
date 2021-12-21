from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
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

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!'})