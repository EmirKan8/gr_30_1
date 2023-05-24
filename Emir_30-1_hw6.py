#Перемножение чисел
def mult(*args):
    n = 1
    for i in args:
        n *= i
    return n
print(mult(2, 3 ,5 ))

#Зеркальная строка
def naoborot(words ='hello'):
    reverse = words[::-1]
    if reverse == words:
        return True
    else:
        return False
print(naoborot())

#Калькулятор
def calculator(n1, operator, n2):
    if operator == '**':
        return round(n1 ** n2, 2)
    elif operator == '+':
        return float(n1 + n2)
    elif operator == '%':
        return n1 % n2
    elif operator == '-':
        return float(n1 - n2)
    elif operator == '*':
        return n1 * n2
    else:
        'false'
print(calculator(2, '**', 3))
print(calculator(5, '+', 9.6))
print(calculator(20, '%', 3))








