# Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени k), не превосходящие числа N.

import math

def degree(N):
    result = []

    for i in range(N):
        if pow(2,  i) <= N:
            result.append(pow(2, i))
    
    print(result)

degree(100)