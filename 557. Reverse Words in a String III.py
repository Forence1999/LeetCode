
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: Leetcode
# @File: Reverse Words in a String III.py
# @Time: 2022/03/06/15:43

import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split(" ")[::-1])[::-1]
    
    
if __name__ == '__main__':
    print('Hello World!')
    
    s = "Let's take LeetCode contest"
    solution = Solution()
    print(solution.reverseWords(s))
    
    print('Brand-new World!')
