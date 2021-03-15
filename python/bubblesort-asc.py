# -*- coding: utf-8 -*-
"""
bubblesort-asc.py - Bubble Sort Algorithm

-----------------------------------------------------------------
This script ranks in ascending order a list of scrambled numbers.

Author:
  Souza, Otávio

History:
  v1.0 2021-03-14, Otávio Souza:
    - Script creation.
"""


def bubbleSort(nList):
    for i in range(len(nList)):
        for j in range(i):
            if (nList[j] > nList[j+1]):
                temp = nList[j]
                nList[j] = nList[j+1]
                nList[j+1] = temp


lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(lista)
print(lista)
