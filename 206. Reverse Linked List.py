
# -*- coding:utf-8 _*-
# @Author: swang
# @Contact: wang00sheng@gmail.com
# @Project Name: LeetCode
# @File: 206. Reverse Linked List.py
# @Time: 2022/03/06/17:28

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
    def reverseList(self, head: ListNode) -> ListNode:
        
        def reverse(node):
            if node.next is None:
                return node, node
            else:
                child, leaf = reverse(node.next)
                child.next = node
                return node, leaf
        
        if head is None:
            return head
        else:
            head, leaf = reverse(head)
            head.next = None
            return leaf
    
    def another(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        from collections import deque
        queue = deque(maxlen=2)
        queue.extend([head, head.next])
        head.next = None
        
        while queue[-1] is not None:
            node = queue.popleft()
            queue.append(queue[-1].next)
            queue[0].next = node
        
        return queue[0]


if __name__ == '__main__':
    print('Hello World!')
    
    vals = [1, 2, 3, 4, 5]
    nodes = [ListNode(val) for val in vals]
    for i, node in enumerate(nodes[:-1]):
        node.next = nodes[i + 1]
    
    root = nodes[0]
    solution = Solution()
    leaf = solution.reverseList(root)
    # leaf = nodes[-1]
    while leaf:
        print(leaf.val)
        leaf = leaf.next
    
    print('Brand-new World!')
