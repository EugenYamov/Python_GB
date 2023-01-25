# Определяем операторы в виде словаря, определим приоритет вычисления
operators = {'+': (1, lambda x, y: x + y),
             '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y),
             '/': (2, lambda x, y: x / y)}

def eval_(formula):
    # Генератор, получает на вход строку, возвращает числа в формате float,
    # операторы и скобки в формате символов.
    def parse(formula_string):
        number = ''
        for s in formula_string:
            if s in '1234567890.': # если символ - цифра, то собираем число
                number += s
            elif number: # если символ не цифра, то выдаём собранное число и начинаем собирать заново
                yield float(number)
                number = ''
            if s in operators or s in "()": # если символ - оператор или скобка, то выдаём как есть
                yield s
        if number: # если в конце строки есть число, выдаём его
            yield float(number)

    # Генератор, получает на вход итерируемый объект из чисел и операторов,
    # возвращает числа и операторы в обратной польской записи.
    def shunting_yard(parsed_formula):
        stack = [] # в качестве стэка используем список
        for token in parsed_formula:
            # если элемент - оператор, то отправляем дальше все операторы из стека,
            # чей приоритет больше или равен пришедшему,
            # до открывающей скобки или опустошения стека.
            # здесь мы пользуемся тем, что все операторы право-ассоциативны
            if token in operators:
                while stack and stack[-1] != "(" and operators[token][0] <= operators[stack[-1]][0]:
                    yield stack.pop()
                stack.append(token)
            elif token == ")":
                # если элемент - закрывающая скобка, выдаём все элементы из стека, до открывающей скобки,
                # а открывающую скобку выкидываем из стека.
                while stack:
                    x = stack.pop()
                    if x == "(":
                        break
                    yield x
            elif token == "(":
                # если элемент - открывающая скобка, просто положим её в стек
                stack.append(token)
            else:
                # если элемент - число, отправим его сразу на выход
                yield token
        while stack:
            yield stack.pop()

    # Функция, получает на вход итерируемый объект чисел и операторов в обратной польской нотации,
    # возвращает результат вычисления:
    def calc(polish):
        stack = []
        for token in polish:
            if token in operators: # если приходящий элемент - оператор
                y, x = stack.pop(), stack.pop() # забираем 2 числа из стека
                stack.append(operators[token][1](x, y)) # вычисляем оператор, возвращаем в стек
            else:
                stack.append(token)
        return stack[0] # результат вычисления - единственный элемент в стеке

    print(calc(shunting_yard(parse(formula))))

eval_(input('Ввод выражения:\n'))