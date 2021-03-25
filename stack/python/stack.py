# -*- coding: utf-8 -*-
"""
stack.py - Stack Data Structure

-----------------------------------------------------------------
Author:
  Souza, Otávio

History:
  v1.0.0 2021-03-14, Otávio Souza:
    - Script creation.
"""


class Stack:
    def __init__(self):
        self.stack = []

    # stack methods
    def empty(self):
        return (len(self.stack) == 0)

    def length(self):
        return len(self.stack)

    def push(self, e):
        self.stack.append(e)

    def remove(self):
        if not self.empty():
            self.stack.pop(len(self.stack) - 1)

    def top(self):
        return self.stack[-1] if not self.empty() else None
