# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 88. Merge Sorted Array.py
# @Time: 2022/04/02/12:06
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m - 1, n - 1
        for tail in range(m + n - 1, -1, -1):
            if p2 == -1 or (p1 != -1 and nums1[p1] > nums2[p2]):
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1


if __name__ == '__main__':
    print('Hello World!')
    
    solution = Solution()
    nums1 = [2, 0]
    m = 1
    nums2 = [1, ]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(nums1)
    print('Brand-new World!')
