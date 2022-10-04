
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: Leetcode
# @File: Delete Node in a Linked List.py
# @Time: 2022/03/06/16:06

import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    print('Hello World!')
    
    vals = [4, 5, 1, 9]
    nodes = [ListNode(val) for val in vals]
    for i, node in enumerate(nodes[:-1]):
        node.next = nodes[i + 1]
    
    root = nodes[0]
    solution = Solution()
    solution.deleteNode(node=root.next)
    
    while root:
        print(root.val)
        root = root.next
    
    print('Brand-new World!')
