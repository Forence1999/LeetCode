# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 78. Subsets4.py
# @Time: 2022/04/02/12:24
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[], ]
        for i in nums:
            res.extend([num + [i] for num in res])
        return res


if __name__ == '__main__':
    print('Hello World!')
    
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
    
    print('Brand-new World!')
