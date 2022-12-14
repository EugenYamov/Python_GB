# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def number_summ(number):
    # Проверяем, является ли введенное число трёхзначным.
    while number // 100 < 1 or number // 100 > 9:
        number = int(input('Неверный ввод числа. Введите трёхзначное число: '))

    summ = 0

    while number > 0:
        digit = number % 10
        summ = summ + digit
        number = number // 10

    print(f"Сумма цифр вашего числа: {summ}")

number_summ(int(input('Введите трёхзначное число: ')))