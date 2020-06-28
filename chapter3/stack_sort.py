#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


def popPush(s1, s2):
    if not s1:
        return -1
    s2.append(s1.pop())


def compare(s1, s2):
    if not s1 or not s2:
        return False
    if s1[-1] < s2[-1]:
        return True
    else:
        return False


def sort(stack_input):
    temp0 = []
    temp1 = []
    popPush(stack_input, temp0)
    while stack_input:
        while compare(stack_input, temp0):
            popPush(temp0, temp1)
        while compare(temp1, stack_input):
            popPush(temp1, temp0)
        popPush(stack_input, temp0)
    while temp1:
        popPush(temp1, temp0)
    return temp0


stack = [1,2,3,4,5,6,7,8,9]
print(stack)
stack = sort(stack)
print(stack)
