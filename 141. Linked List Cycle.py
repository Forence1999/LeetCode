# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 141. Linked List Cycle.py
# @Time: 2022/04/01/21:04
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True


if __name__ == '__main__':
    print('Hello World!')
    
    print('Brand-new World!')
