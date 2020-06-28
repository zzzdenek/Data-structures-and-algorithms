#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None # the pointer initially points to nothing

def traverse(root):
  node = root
  next_node = None
  prev_node = None
  while node != None:
    next_node = node.next
    node.next = prev_node
    prev_node = node
    node = next_node
  return prev_node

root = Node(10)
node1 = Node(11)
node2 = Node(12)
node3 = Node(13)
node4 = Node(14)

root.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

node = root
while node:
    print(node.value)
    node = node.next

root = traverse(root)

node = root
while node:
    print(node.value)
    node = node.next
