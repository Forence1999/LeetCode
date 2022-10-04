
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 104. Maximum Depth of Binary Tree.py
# @Time: 2022/04/01/22:13

import os, sys
import time
import random
import warnings
import numpy as np


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            l_height = self.maxDepth(root.left)
            r_height = self.maxDepth(root.right)
            return max(l_height, r_height) + 1


if __name__ == '__main__':
    print('Hello World!')
    
    print('Brand-new World!')
