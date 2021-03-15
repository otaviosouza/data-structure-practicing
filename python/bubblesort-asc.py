# -*- coding: utf-8 -*-
"""
bubblesort-asc.py - Bubble Sort Algorithm

-----------------------------------------------------------------
This script ranks in ascending order a list of scrambled numbers.

Author:
  Souza, Otávio

History:
  v1.0.1 2021-03-14, Otávio Souza:
    - Swap improvement. Using two simultaneous assignments.
    - Correcting outer 'for'. Pass amount controller.
  v1.0.0 2021-03-14, Otávio Souza:
    - Script creation.
"""


def bubbleSort(nList):
    for i in range(len(nList)-1, 0, -1):
        for j in range(i):
            if (nList[j] > nList[j+1]):
                nList[j], nList[j+1] = nList[j+1], nList[j]


lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(lista)
print(lista)
