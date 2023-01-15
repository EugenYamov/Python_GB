# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(a, b):
    if (b == 1):
        return a
    if (b != 1):
        return (a * exponentiation(a, b - 1))

a = int(input("Введите число: "))
b = int(input("Введите степень: "))

print(f"Число {a} в степени {b} равно: {exponentiation(a, b)}")