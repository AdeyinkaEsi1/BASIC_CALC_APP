
def mat_operation(inp1, operator, inp2):
    if operator == '+':
        return inp1 + inp2
    elif operator == '-':
        return inp1 - inp2
    elif operator == '/':
        if inp2 != 0:  # Check for division by zero
            return inp1 / inp2
        else:
            return 'Error: Division by zero'
    elif operator == '*':
        return inp1 * inp2
    else:
        return 'Error: Invalid operator'
