# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь вводит натуральное число N – количество элементов в массиве. 
# и число, которое необходимо проверить - X.

from random import randint

def search_match_in_list(n, x):
    list = [randint(1, 5) for i in range(n)]
    counter = 0
    
    for i in list:

        if x == i: counter += 1
    
    print(f'Колличество значений ({x}) в массиве {list} = {counter}')

search_match_in_list(int(input('Введите колличество элементов массива: ')),
                    int(input('Введите значение, которое нужно подсчитать: ')))