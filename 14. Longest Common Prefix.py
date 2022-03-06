# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: Leetcode
# @File: Longest Common Prefix.py
# @Time: 2022/03/06/16:21
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = 200
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
        for i in range(1, min_len + 1):
            for j in range(len(strs) - 1):
                if strs[j][:i] != strs[j + 1][:i]:
                    return strs[j][:i -1]
        return strs[0][:min_len]


if __name__ == '__main__':
    print('Hello World!')
    
    ls = ["flower", "flow", "flight"]
    ls = ["ab", "b"]
    solution = Solution()
    print(solution.longestCommonPrefix(ls))
    
    print('Brand-new World!')
