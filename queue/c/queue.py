# -*- coding: utf-8 -*-
"""
queue.py - Queue Data Structure

-----------------------------------------------------------------
A simple study of queue data structure

Author:
  Souza, Otávio

History:
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
