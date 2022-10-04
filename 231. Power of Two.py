
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 231. Power of Two.py
# @Time: 2022/03/06/17:00

import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0


if __name__ == '__main__':
    print('Hello World!')
    
    n = 16
    solution = Solution()
    print(solution.isPowerOfTwo(n))
    
    print('Brand-new World!')
