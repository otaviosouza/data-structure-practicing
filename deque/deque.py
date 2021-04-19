#!python3
# -*- coding: utf-8 -*-
"""
deque.py - Deque Data Structure
It is a generalized version of Queue data structure that allows
insert and delete at both ends.

-----------------------------------------------------------------
Author:
  Souza, Otávio

History:
  v1.0.1 2021-03-25, Otávio Souza:
    - Replace string output by fstring.
    - Description improvement for better understanding.
  
  v1.0.0 2021-03-15, Otávio Souza:
    - Script creation.
"""


class Deque:
    def __init__(self):
        self.deque = []
        self.lenDeque = 0

    # deque methods
    def empty(self):
        return (self.lenDeque == 0)

    def length(self):
        return self.lenDeque

    def push_front(self, e):
        self.deque.insert(0, e)
        self.lenDeque += 1

    def push_back(self, e):
        self.deque.insert(self.lenDeque, e)
        self.lenDeque += 1

    def remove_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.lenDeque -= 1

    def remove_back(self):
        if not self.empty():
            self.deque.pop(self.lenDeque - 1)
            self.lenDeque -= 1

    def front(self):
        return self.deque[0] if not self.empty() else None

    def back(self):
        return self.deque[-1] if not self.empty() else None

    def show(self):
        for i in self.deque:
            print(i, end=' ')


# testing deque
d = Deque()

# insertion tests
d.push_front(10)  # 10
d.push_front(5)  # 5 10
d.push_back(20)  # 5 10 20
d.push_front(7)  # 7 5 10 20
d.push_back(40)  # 7 5 10 20 40

d.show()  # 7 5 10 20 40

print(f'\nfront: {d.front()}')  # 7
print(f'\nback: {d.back()}')  # 40

# removal test
d.remove_back()  # remove 40 | remaining 7 5 10 20
d.remove_front()  # remove 7 | remaining 5 10 20
d.show()  # 5 10 20
print(f'\nfront: {d.front()}')  # 5
print(f'\nback: {d.back()}')  # 20
