# -*- coding: utf-8 -*-
"""7

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dGj6Ar4isfDQARrkUd2fiLjxqi0hpprr
"""

import array as arr

numbers = 10,20,30,40,50,60,70,80,90

n = int(input("Выберите номер элемента: "))
a = int(input("Выберите эелемент n по b: "))
b = int(input("Выберите элемент b по n:  "))
h = int(input("Выберете шаг поиска элементов с b по n:  "))
i = int(input("Выберите элемент i:  "))


class elemen_po_vubory:
    print(numbers[n-1])


class elemen_neskolko:
    print(numbers[a-1:b-1:h])

class elemen_po_konets:
    print(numbers[-i])