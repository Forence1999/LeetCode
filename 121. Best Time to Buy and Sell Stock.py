# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 121. Best Time to Buy and Sell Stock.py
# @Time: 2022/04/02/11:31
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit


if __name__ == '__main__':
    print('Hello World!')
    
    print('Brand-new World!')
