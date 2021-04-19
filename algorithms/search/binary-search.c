/*************************************************************
* binary-search.c - Binary Search Algorithm                  *
* Implements a bynary search algorithm                       *
* Author:                                                    *
*   Souza, Otávio                                            *
* History:                                                   *
*   v1.0.0 2021-04-18, Otávio Souza                          *
*       - first release                                      *
**************************************************************/

#include <stdio.h>

void bubbleSort(int *list, int length);
int binarySearch(int list[], int length, int target);
int main(void)
{
    int target, pos;
    int lista[] = {54, 26, 93, 17, 77, 31, 44, 55, 20};
    int len = sizeof lista / sizeof lista[0];

    printf("which number do you want to find? ");
    scanf("%d", &target);

    pos = binarySearch(lista, len, target);

    (pos != -1) ? printf("Found. Position: %d\n", pos) : printf("Not found.\n");

    return 0;
}

void bubbleSort(int *list, int length)
{
    int aux;
    for (int i = 1; i < length; i++)
    {
        for (int j = 0; j < (length - 1); j++)
        {
            if (list[j] > list[j + 1])
            {
                aux = list[j];
                list[j] = list[j + 1];
                list[j + 1] = aux;
            }
        }
    }
}

int binarySearch(int list[], int length, int target)
{
    int first = 0, last = length - 1;
    int mid;

    bubbleSort(list, length);

    while (first <= last)
    {
        mid = (first + last) / 2;
        if (target == list[mid])
        {
            return mid;
        }
        else if (target < list[mid])
        {
            last = mid - 1;
        }
        else
        {
            first = mid + 1;
        }
    }
    return -1;
}