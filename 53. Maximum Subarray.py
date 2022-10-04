
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 53. Maximum Subarray.py
# @Time: 2022/04/02/11:47

import os, sys
import time
import random
import warnings
import numpy as np
from typing import List


class Solution:  # based on the idea of "121. Best Time to Buy and Sell Stock"
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        min_price = 0
        max_profit = nums[0]
        for price in nums:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit


class Solution_Dp:  # dynamic programming
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        maxAns = nums[0]
        for x in nums:
            pre = max(pre + x, x)
            maxAns = max(maxAns, pre)
        return maxAns


if __name__ == '__main__':
    print('Hello World!')
    
    print('Brand-new World!')
