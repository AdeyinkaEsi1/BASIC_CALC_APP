# from django.shortcuts import render
# from django.http import HttpResponse
# from .utils import mat_operation


# def calculator(request):
#     result = None

#     if request.method == 'POST':
#         try:
#             inp1 = int(request.POST['input1'])
#             operator = request.POST['operator']
#             inp2 = int(request.POST['input2'])
            
#             result = mat_operation(inp1, operator, inp2)

#             if isinstance(result, (int, float)):
#                 # print(f'Result: {result}')
#                 pass
#             else:
#                 result = f'Error: {result}'
#         except ValueError as ve:
#             result = f'Error: Invalid input. Please enter valid numbers.'
#             # -- {ve}
#         except Exception as e:
#             result = f'Error!: {e}'
    

#     return render(request, 'EasyCalc/index.html', {'result': result})



from django.shortcuts import render
from .utils import mat_operation

def calculator(request):
    result = None

    if request.method == 'POST':
        try:
            # Get the expression and operator from the UI
            expression = request.POST.get('expression', '')
            operator = request.POST.get('operator', '')

            # Assuming your 'mat_operation' function can handle an expression string
            result = mat_operation(expression, operator)

            if isinstance(result, (int, float)):
                # Successful calculation
                pass
            # else:
            #     result = f'Error: {result}'
        except Exception as e:
            result = f'Error: {e}'

    return render(request, 'EasyCalc/index.html', {'result': result})


# if __name__ == "__main__":
#     calculator()

