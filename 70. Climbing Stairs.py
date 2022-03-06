# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 70. Climbing Stairs.py
# @Time: 2022/04/01/21:48
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np


class Solution:
    
    def climbStairs(self, n: int) -> int:
        p = 0
        q = 0
        r = 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r


if __name__ == '__main__':
    print('Hello World!')
    
    solution = Solution()
    for i in range(10):
        print(solution.climbStairs(i))
    
    print('Brand-new World!')
