from django.shortcuts import render
from django.http import HttpResponse
from .utils import mat_operation


def calculator(request):
    result = None

    if request.method == 'POST':
        try:
            inp1 = int(request.POST['input1'])
            operator = request.POST['operator']
            inp2 = int(request.POST['input2'])
            
            result = mat_operation(inp1, operator, inp2)

            if isinstance(result, (int, float)):
                # print(f'Result: {result}')
                pass
            else:
                result = f'Error: {result}'
        except ValueError as ve:
            result = f'Error: Invalid input. Please enter valid numbers.'
            # -- {ve}
        except Exception as e:
            result = f'Error!: {e}'
    

    return render(request, 'EasyCalc/index.html', {'result': result})


# if __name__ == "__main__":
#     calculator()

