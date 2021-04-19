# -*- coding: utf-8 -*-
'''
linked_list.py - Linked list Data Structure
A linear data structure in which the elements are not stored at
contiguous memory locations. The elements in a linked list are linked
using pointers.


----------------------------------------------------------------------
Author:
    Souza, Otávio

History:
    v1.0.1 2021-03-25, Otávio Souza:
        - Replace string output by fstring.
        - Description improvement for better understanding.
    v1.0.0 2021-03-15, Otávio Souza:
        - Script creation.
'''


class Node:
    def __init__(self, label):
        self.label = label
        self.near = None

    def getLabel(self):
        return self.label

    def setLabel(self, label):
        self.label = label

    def getNear(self):
        return self.near

    def setNear(self, near):
        self.near = near


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):
        if index >= 0:
            # creates a new node
            node = Node(label)
            # check if it is an empty list
            if self.empty():
                self.first = node
                self.last = node
            else:
                if index == 0:
                    # push in beginning
                    node.setNear(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # push in end
                    self.last.setNear(node)
                    self.last = node
                else:
                    # push in middle
                    prev_node = self.first
                    curr_node = self.first.getNear()
                    curr_index = 1

                    while curr_node is not None:
                        if curr_index == index:
                            # setting curr_node as next node
                            node.setNear(curr_node)
                            # setting node as next of prev_node
                            prev_node.setNear(node)
                            break
                        prev_node = curr_node
                        curr_node = curr_node.getNear()
                        curr_index += 1
            # update list length
            self.len_list += 1

    def pop(self, index):
        if not self.empty() and 0 <= index < self.len_list:
            flag_remove = False
            if self.first.getNear() is None:
                # has only one element
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # remove from beginning, more than one element
                self.first = self.first.getNear()
                flag_remove = True
            else:
                # more than one element; removal not in beginning
                prev_node = self.first
                curr_node = self.first.getNear()
                curr_index = 1

                while curr_node is not None:
                    if index == curr_index:
                        prev_node.setNear(curr_node.getNear())
                        curr_node.setNear(None)
                        flag_remove = True
                        break
                    prev_node = curr_node
                    curr_node = curr_node.getNear()
                    curr_index += 1
            if flag_remove:
                self.len_list -= 1

    def empty(self):
        return self.first is None

    def length(self):
        return self.len_list

    def show(self):
        curr_node = self.first

        while curr_node is not None:
            print(curr_node.getLabel(), end=' ')
            curr_node = curr_node.getNear()
        print('')


lista = LinkedList()

# teste inserção
lista.push('Marcos', 0)  # inserção no início
lista.show()
lista.push('Maria', 1)  # inserção no final
lista.show()
lista.push('Yankee', 0)  # inserção no início
lista.show()
lista.push('Catarina', 2)  # inserção no meio
lista.show()
lista.push('Lilica', 4)  # inserção no final
lista.show()
lista.push('Sara', 2)  # inserção no meio
lista.show()
print(f'Tamanho da lista: {lista.length()}\n')

# teste remoção
lista.pop(0)  # remoção do início
lista.show()
lista.pop(2)  # remoção do meio
lista.show()
lista.pop(3)  # remoção do final
lista.show()
print(f'Tamanho da lista: {lista.length()}\n')
