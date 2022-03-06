# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: Leetcode
# @File: Add Two Numbers.py
# @Time: 2022/03/06/15:45
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        carry = val = 0
        
        while carry or l1 or l2:
            val = carry
            
            if l1:
                l1, val = l1.next, l1.val + val
            if l2:
                l2, val = l2.next, l2.val + val
            
            carry, val = divmod(val, 10)
            curr.next = curr = ListNode(val)
        
        return head.next
    
    def another(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = l1
        carry = 0
        while l1 is not None:
            
            carry = l1.val + l2.val + carry if l2 is not None else carry + l1.val
            l1.val, carry = carry % 10, carry // 10
            
            l2 = l2.next if l2 is not None else None
            if l1.next is None:
                l1.next = l2
                l2 = None
            fa = l1
            l1 = l1.next
        if carry != 0:
            fa.next = ListNode(val=carry, next=None)
        return res


if __name__ == '__main__':
    print('Hello World!')
    
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
    solution = Solution()
    res = solution.addTwoNumbers(l1, l2)
    while res is not None:
        print(res.val)
        res = res.next
    
    print('Brand-new World!')
