# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: Leetcode
# @File: Median of Two Sorted Arrays.py
# @Time: 2022/03/06/13:50
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
    
    def another(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]


if __name__ == '__main__':
    print('Hello World!')
    
    s = ["h", "e", "l", "l", "o"]
    solution = Solution()
    solution.reverseString(s)
    print(s)
    
    print('Brand-new World!')
