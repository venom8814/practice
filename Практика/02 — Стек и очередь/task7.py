def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()

    for token in tokens:
        if token.isdigit() or '.' in token:
            output.append(token)
        elif token in precedence:
            while (stack and stack[-1] in precedence and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # убираем '('

    while stack:
        output.append(stack.pop())

    return ' '.join(output)


def evaluate_postfix(postfix_expr):
    stack = []
    tokens = postfix_expr.split()

    for token in tokens:
        if token in '+-*/^':
            b = float(stack.pop())
            a = float(stack.pop())
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)
        else:
            stack.append(float(token))

    return stack[0]


def calculator(infix_expr):
    try:
        postfix = infix_to_postfix(infix_expr)
        result = evaluate_postfix(postfix)
        return result, postfix
    except Exception as e:
        return f"Ошибка: {e}", ""


if __name__ == "__main__":

    expressions = [
        "3 + 4 * 2",
        "( 3 + 4 ) * 2",
        "5 * ( 3 + 2 )",
        "10 / 2 + 3",
        "2 ^ 3 + 1"
    ]

    for expr in expressions:
        result, opn = calculator(expr)
        print(f"Выражение: {expr}")
        print(f"ОПН: {opn}")
        print(f"Результат: {result}\n")