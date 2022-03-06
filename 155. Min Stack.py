# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 155. Min Stack.py
# @Time: 2022/04/01/20:39
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
import math


class MinStack_asynchronous:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]
    
    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self) -> None:
        if self.stack[-1] <= self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]
    
    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]


if __name__ == '__main__':
    print('Hello World!')
    
    print('Brand-new World!')
