# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 217. Contains Duplicate.py
# @Time: 2022/03/06/17:17
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
    
    def another(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


if __name__ == '__main__':
    print('Hello World!')
    
    ls = [1, 2, 3, 1]
    solution = Solution()
    print(solution.containsDuplicate(ls))
    
    print('Brand-new World!')
