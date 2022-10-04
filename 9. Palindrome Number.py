
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: Leetcode
# @File: Palindrome Number.py
# @Time: 2022/03/06/16:10

import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy


class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    def another(self, x: int) -> bool:
        s = str(x)
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True


if __name__ == '__main__':
    print('Hello World!')
    
    x = 121
    solution = Solution()
    print(solution.isPalindrome(x))
    
    print('Brand-new World!')
