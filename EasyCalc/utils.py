
# def mat_operation(expression, operator):
#     try:
#         # Split the expression into operands
#         operands = [float(operand) for operand in expression.split('+')]

#         # Apply the operator between operands
#         if operator == '-':
#             result = operands[0] - sum(operands[1:])
#         elif operator == '/':
#             # Check for division by zero
#             if 0 in operands[1:]:
#                 return 'Error: Division by zero'
#             result = operands[0] / operands[1]
#         elif operator == '*':
#             result = operands[0] * operands[1]
#         elif operator == '+':
#             result = sum(operands)
#         else:
#             return 'Error: Invalid operator'

#         return result
#     except ValueError:
#         return 'Error: Invalid input. Please enter valid numbers.'
#     except Exception as e:
#         return f'Error: {e}'
