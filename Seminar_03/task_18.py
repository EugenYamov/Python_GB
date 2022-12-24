# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит натуральное число N – количество элементов в массиве. 
# и число, которое необходимо проверить - X.

from random import randint

def closer_element_in_list(n, x):
    list = list = [randint(1, 100) for i in range(n)]
    print(f'Ваш массив: {list}')

    list_diff = sorted(list)

    min_element = x - list_diff[0]
    
    for i in range(len(list_diff)):

        if min_element > abs(x - list_diff[i]):
            min_element = x - list_diff[i]
    
    print(f'Ближайшее значение к вашему числу: {x-min_element}')
        
closer_element_in_list(int(input('Введите количество элементов массива: ')),\
                    int(input('Введите число: ')))