
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 136. Single Number.py
# @Time: 2022/04/01/20:47

import os, sys
import time
import random
import warnings
import numpy as np
from typing import List
from functools import reduce


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    print('Hello World!')
    
    print('Brand-new World!')
