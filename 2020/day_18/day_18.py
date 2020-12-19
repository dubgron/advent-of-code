#!/mnt/d/software/python/python.exe -B

input_file = open('day_18_input.txt', 'r')
input_data = [line.strip() for line in input_file]

def rpn(equation, precedence):
    output = []
    operator = []
    for token in equation:
        if token.isdigit():
            output.append(token)
        elif token in ('+', '*'):
            while len(operator) and precedence(operator[-1], token) and operator[-1] != '(':
                output.append(operator.pop())
            operator.append(token)
        elif token == '(':
            operator.append(token)
        elif token == ')':
            while len(operator) and operator[-1] != '(':
                output.append(operator.pop())
            if len(operator) and operator[-1] == '(':
                operator.pop()
    while len(operator):
        output.append(operator.pop())

    result = []
    for token in output:
        if token.isdigit():
            result.append(int(token))
        elif token == '+':
            result.append(result.pop() + result.pop())
        elif token == '*':
            result.append(result.pop() * result.pop())
    return result[0]

# Part One

total = sum([rpn(line, lambda x, y: True) for line in input_data])
print(total)

# Part Two

total = sum([rpn(line, lambda x, y: x >= y) for line in input_data])
print(total)
