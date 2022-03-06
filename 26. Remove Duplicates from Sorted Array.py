# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 26. Remove Duplicates from Sorted Array.py
# @Time: 2022/03/06/18:29
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        
        return slow
    
    def another(self, nums: List[int]) -> int:
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == nums[idx + 1]:
                nums.pop(idx)
            else:
                idx += 1
        
        return len(nums)


if __name__ == '__main__':
    print('Hello World!')
    
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    solution = Solution()
    print(solution.removeDuplicates(nums), nums)
    
    print('Brand-new World!')
