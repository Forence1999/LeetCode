# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 169. Majority Element.py
# @Time: 2022/03/06/18:14
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]
        
        for i in nums:
            if count == 0:
                candidate = i
            count += 1 if i == candidate else -1
        return candidate


if __name__ == '__main__':
    print('Hello World!')
    
    nums = [3, 2, 3]
    solution = Solution()
    print(solution.majorityElement(nums))
    
    print('Brand-new World!')
