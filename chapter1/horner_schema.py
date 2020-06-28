#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

n = 2
x = 5
A = [ -6, -3, 4]

y = 0
for i in range(n, -1, -1):
  y = A[i] + x * y
print(y)
