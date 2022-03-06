# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: Leetcode
# @File: Longest Palindromic Substring.py
# @Time: 2022/03/06/15:44
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy


class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        for i in range(len(s) - 1):
            l1, r1 = self.expandAroundCenter(s, i, i)
            l2, r2 = self.expandAroundCenter(s, i, i + 1)
            if r1 - l1 + 1 > right - left + 1:
                left, right = l1, r1
            if r2 - l2 + 1 > right - left + 1:
                left, right = l2, r2
        return s[left:right + 1]
    
    def expandAroundCenter(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1


if __name__ == '__main__':
    print('Hello World!')
    
    s = 'babad'
    solution = Solution()
    print(solution.longestPalindrome(s))
    
    print('Brand-new World!')
