# -*- coding: utf-8 -*-
"""
queue.py - Queue Data Structure
A linear structure which follows a particular order in which
the operations are performed: First In First Out (FIFO).

----------------------------------------------------------------------
Author:
  Souza, Otávio

History:
  v1.0.1 2021-03-25, Otávio Souza:
    - Description improvement for better understanding.
  
  v1.0.0 2021-03-14, Otávio Souza:
    - Script creation.
"""


class Queue:
    def __init__(self):
        self.queue = []
        self.lenQueue = 0

    # queue methods
    def empty(self):
        return (self.lenQueue == 0)

    def length(self):
        return self.lenQueue

    def push(self, e):
        self.queue.append(e)
        self.lenQueue += 1

    def remove(self):
        if not self.empty():
            self.queue.pop(0)
            self.lenQueue -= 1

    def front(self):
        return self.queue[0] if not self.empty() else None
