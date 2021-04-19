/*************************************************************
* bubble-sort_desc.c - Bubble Sort Algorithm                  *
* Implements a bubble sort algorithm which ranks             *
* in descending order a list of scrambled numbers.           *
* History:                                                   *
*   v1.0.0 2021-04-18, Otávio Souza                          *
*       - first release                                      *
**************************************************************/

#include <stdio.h>

int main(void)
{
    int lista[] = {54, 26, 93, 17, 77, 31, 44, 55, 20};
    int len = sizeof lista / sizeof lista[0];
    int aux;

    for (int i = 1; i < len; i++)
    {
        for (int j = 0; j < (len - 1); j++)
        {
            if (lista[j] < lista[j + 1])
            {
                aux = lista[j];
                lista[j] = lista[j + 1];
                lista[j + 1] = aux;
            }
        }
    }

    for (int i = 0; i < len; i++)
    {
        i != (len - 1) ? printf("%d ", lista[i]) : printf("%d\n", lista[i]);
    }

    return 0;
}
