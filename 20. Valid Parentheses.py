# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 20. Valid Parentheses.py
# @Time: 2022/03/06/18:20
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack


if __name__ == '__main__':
    print('Hello World!')
    
    s = "()[]{}"
    solution = Solution()
    print(solution.isValid(s))
    
    print('Brand-new World!')
