# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: Leetcode
# @File: Nim Game.py
# @Time: 2022/03/06/16:00
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4!=0
    
if __name__ == '__main__':
    print('Hello World!')

    n = 4
    solution = Solution()
    print(solution.canWinNim(n))
    
    print('Brand-new World!')
