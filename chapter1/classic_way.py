#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

n = 2
x = 5
A = [ -6, -3, 4]

y = 0
for k in range(n+1):
  temp = x
  if k > 1:
    for i in range(k-1):
      temp *= x
  elif k == 0:
    temp = 1
  y += A[k] * temp
print(y)
