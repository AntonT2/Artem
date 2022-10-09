from django.http import HttpResponse
from django.shortcuts import render
inf={
   'info1':'Я рома',
    'info2':'Меня зовут Олег',
    'info3':'Мне 24'
}

def first_page(request):
    return HttpResponse('Hello Django')


def info(request):
    return HttpResponse('<h1>Моё хобби:Жить</h1>')


def main_page(request):
    return render(request, 'index.html')
def about(request):
    return render(request,'about.html',context=inf)
def Paris(request):
    return render(request,'Paris.html')
def Barselona(request):
    return render(request,'Barselona.html')
def Rim(request):
    return render(request,'Rim.html')
