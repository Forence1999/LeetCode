
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 46. Permutations.py
# @Time: 2022/04/02/12:31

import os, sys
import time
import random
import warnings
import numpy as np
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            temp = []
            for j in res:
                for k in range(len(j) + 1):
                    temp.append(j[:k] + [i] + j[k:])
            res = temp
        return res


if __name__ == '__main__':
    print('Hello World!')
    
    solution = Solution()
    print(solution.permute([1, 2, 3, 4, 5]))
    print('Brand-new World!')
