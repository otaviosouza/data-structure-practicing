# -*- coding: utf-8 -*-
"""
stack-impr.py - Stack Data Structure

-----------------------------------------------------------------
Author:
  Souza, Otávio

History:
  v1.0.1 2021-03-14, Otávio Souza:
    - Script improvement.
  v1.0.0 2021-03-14, Otávio Souza:
    - Script creation.
"""


class Stack:
    def __init__(self):
        self.stack = []
        self.lenStack = 0

    # stack methods
    def empty(self):
        return (self.lenStack == 0)

    def length(self):
        return self.lenStack

    def push(self, e):
        self.stack.append(e)
        self.lenStack += 1

    def remove(self):
        if not self.empty():
            self.stack.pop(len(self.stack) - 1)
            self.lenStack -= 1

    def top(self):
        return self.stack[-1] if not self.empty() else None
