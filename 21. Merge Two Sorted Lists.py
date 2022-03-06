# !/usr/bin/env python
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 21. Merge Two Sorted Lists.py
# @Time: 2022/03/06/18:24
# @Software: PyCharm
import os, sys
import time
import random
import warnings
import numpy as np
from copy import deepcopy


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    print('Hello World!')
    
    print('Brand-new World!')
