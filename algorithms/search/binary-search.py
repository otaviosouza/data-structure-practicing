#!python3
# -*- coding: utf-8 -*-
"""
binary-search.py - Binary Search Algorithm
Implements a bynary search algorithm.

-----------------------------------------------------------------
Author:
  Souza, Otávio

History:
  v1.0.0 2021-03-14, Otávio Souza:
    - Script creation.
"""


def bubbleSort(nList):
    for i in range(len(nList)-1, 0, -1):
        for j in range(i):
            if (nList[j] > nList[j+1]):
                nList[j], nList[j+1] = nList[j+1], nList[j]


def binarySearch(nList, nTarget):
    first, mid = 0, 0
    last = len(nList) - 1
    found = True
    bubbleSort(nList)
    while (first <= last):
        mid = (first + last) // 2
        if nTarget == nList[mid]:
            return found
        if (nTarget < nList[mid]):
            last = mid - 1
        else:
            first = mid + 1
    return not found


def main():
    lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    answer = "Found" if binarySearch(lista, 26) else "Not found"

    print(answer)


main()
