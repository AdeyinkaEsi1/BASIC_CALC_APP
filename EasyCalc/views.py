
from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
    result = None

    return render(request, 'EasyCalc/index.html', {'result': result})



