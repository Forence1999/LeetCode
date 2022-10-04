
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 160. Intersection of Two Linked Lists.py
# @Time: 2022/04/01/20:30

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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A


if __name__ == '__main__':
    print('Hello World!')
    
    print('Brand-new World!')
