#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
binary-search-tree.py - Binary Search Tree
Implements a bynary search tree.

------------------------------------------------------------
Author:
  Souza, Otávio

Changelog:
  v1.0 2021-09-07, Otávio Souza:
    - Class Node, Class BinarySearchTree.
    - Insert method
  
  v1.1 2021-09-07, Otávio Souza:
    - Remove method
"""

class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None
        
    def setLabel(self, label):
        self.label = label
    def setLeft(self, left):
        self.left = left
    def setRight(self, right):
        self.right = right

    def getLabel(self):
        return self.label
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def empty(self):
        return True if (self.root == None) else False

    def insert(self, label):
        """Insert an element on the left or right"""
        # new node
        node = Node(label)

        # empty tree?
        if self.empty():
            self.root = node
        else:
            # insert recursive
            dad_node = None
            curr_node = self.root

            while True:
                if curr_node != None:
                    dad_node = curr_node

                    # left or right?
                    curr_node = curr_node.getLeft() if (node.getLabel() < curr_node.getLabel()) else curr_node.getRight()
                else:
                    # insert here
                    dad_node.setLeft(node) if (node.getLabel() < dad_node.getLabel()) else dad_node.setRight(node)
                    break
    
    def remove(self, label):
        """
        Remove an element
        
        Case 1. leaf node
        Case 2. one child
        Case 3. two children
        """

        dad_node = None
        curr_node = self.root

        while curr_node != None:
            if label == curr_node.getLabel():
                #leaf node
                if (curr_node.getLeft() == None and curr_node.getRight() == None):
                    #is root?
                    if dad_node == None:
                        self.root = None
                    else:
                        dad_node.setLeft(None) if (dad_node.getLeft() == curr_node) else dad_node.setRight(None)
                
                #one child node
                elif (curr_node.getLeft() == None and curr_node.getRight() != None) or \
                    (curr_node.getLeft() != None and curr_node.getRight() == None):
                    
                    #is root?
                    if dad_node == None:
                        self.root = curr_node.getLeft() if (curr_node.getLeft() != None) else curr_node.getRight()
                    else:
                        # is curr_node's child at left?
                        if curr_node.getLeft() != None:
                            # is curr_node child at left?
                            dad_node.setLeft(curr_node.getLeft()) \
                                if (dad_node.getLeft() and (dad_node.getLeft().getLabel() == curr_node.getLabel())) \
                                else dad_node.setRight(curr_node.getLeft())
                        else:
                            dad_node.setLeft(curr_node.getRight()) \
                                if (dad_node.getLeft() and (dad_node.getLeft().getLabel() == curr_node.getLabel())) \
                                else dad_node.setRight(curr_node.getRight())
                # two children
                elif (curr_node.getLeft() != None and curr_node.getRight() != None):
                    dad_smaller_node = curr_node
                    smaller_node = curr_node.getRight()
                    next_smaller =curr_node.getRight().getLeft()

                    while next_smaller != None:
                        dad_smaller_node = smaller_node
                        smaller_node = next_smaller
                        next_smaller =smaller_node.getLeft()
                    
                    if dad_node == None:
                        if self.root.getRight().getLabel() == smaller_node.getLabel():
                            smaller_node.setLeft(self.root.getLeft())
                        else:
                            if dad_smaller_node.getLeft() and \
                                dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
                                dad_smaller_node.setLeft(None)
                            else:
                                dad_smaller_node.setRight(None)
                            smaller_node.setLeft(curr_node.getLeft())
                            smaller_node.setRight(curr_node.getRight())
                        self.root = smaller_node
                    else:
                        if dad_node.getLeft() and dad_node.getLeft().getLabel() == curr_node.getLabel():
                            dad_node.setLeft(smaller_node)
                        else:
                            dad_node.setRight(smaller_node)
                        
                        if dad_smaller_node.getLeft() and \
                            dad_smaller_node.getLeft().getLabel() == smaller_node.getLabel():
                            dad_smaller_node.setLabel(None)
                        else:
                            dad_smaller_node.setRight(None)
                        
                        
                        smaller_node.setLeft(curr_node.getLeft())
                        smaller_node.setRight(curr_node.getRight())
                break
            dad_node = curr_node

            curr_node = curr_node.getLeft() if label < curr_node.getLabel() else curr_node.getRight()



    def getRoot(self):
        return self.root
    
    def show(self, curr_node):
        """Show in pre-order (root - left - right)"""
        if curr_node != None:
            print('{}'.format(curr_node.getLabel()), end=' ')
            self.show(curr_node.getLeft())
            self.show(curr_node.getRight())
    

bst = BinarySearchTree()

bst.insert(8)
bst.insert(3)
bst.insert(1)
bst.insert(6)
bst.insert(4)
bst.insert(7)
bst.insert(10)
bst.insert(14)
bst.insert(13)

#bst.show(bst.getRoot())

bst.remove(1)
#bst.show(bst.getRoot()) #8, 3, 6, 4, 7, 10, 14, 13

bst.remove(10)
#bst.show(bst.getRoot()) #8, 3, 6, 4, 7, 14, 13

bst.remove(6)
#bst.show(bst.getRoot()) #8, 3, 7, 4, 14, 13

bst.remove(8)
bst.show(bst.getRoot()) #13, 3, 7, 4, 14