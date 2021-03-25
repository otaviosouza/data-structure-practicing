#!python3
# -*- coding: utf-8 -*-
"""
deque.py - Deque Data Structure
Deque using the module “collections“.
Deque is preferred over list in the cases where we need quicker append
and pop operations from both the ends of container.

----------------------------------------------------------------------
Author:
  Souza, Otávio

History:
  v1.0.1 2021-03-25, Otávio Souza:
    - Description improvement for better understanding.
  
  v1.0.0 2021-03-15, Otávio Souza:
    - Script creation.
"""

from collections import deque

d = deque()
d.append(1)
d.appendleft(2)
d.append(3)
d.appendleft(4)

for i in d:
    print(i, end=' ')  # 4, 2, 1, 3

d.pop()
d.popleft()
d.remove(1)

for i in d:
    print(i, end=' ')  # 2
