# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: Leetcode
# @File: Lowest Common Ancestor of a Binary Search Tree.py
# @Time: 2022/03/06/15:48
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return root if (root.val - p.val) * (root.val - q.val) <= 0 else self.lowestCommonAncestor(
            root.left if root.val > p.val else root.right, p, q)


if __name__ == '__main__':
    print('Hello World!')
    
    vals = [6, 2, 8, 0, 4, 7, 9, 'null', 'null', 3, 5]
    root = TreeNode(vals[0])
    nodes = [root]
    i = -1
    while nodes != []:
        node = nodes.pop(0)
        if node is None:
            continue
        else:
            if vals[i] == 'null':
                nodes.append(None)
            else:
                node.left = TreeNode(vals[i])
            if vals[i + 1] == 'null':
                nodes.append(None)
            else:
                node.right = TreeNode(vals[i + 1])
            i += 2
    
    p = root.left
    q = root.right
    
    solution = Solution()
    print(solution.lowestCommonAncestor(root, p, q).val)
    
    print('Brand-new World!')
