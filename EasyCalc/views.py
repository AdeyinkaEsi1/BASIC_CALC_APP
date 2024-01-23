
from django.shortcuts import render
from django.http import HttpResponse

def calculator(request):
    result = None

    return render(request, 'EasyCalc/index.html', {'result': result})


if __name__ == "__main__":
    calculator() # type: ignore

