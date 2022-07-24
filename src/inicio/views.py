from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myHomeView(request,*args, **kwargs):
    myContext = {
            'myText': 'esto es sobre nosotros',
            'myNumber': 123,
            }
    return render(request,"contenido.html",myContext)
    #return HttpResponse('<h1>Hola Mundo Django</h1>')
def anotherView(request):
    print(request.user)
    return HttpResponse('<h1>Esta es otra vista</h1>')

