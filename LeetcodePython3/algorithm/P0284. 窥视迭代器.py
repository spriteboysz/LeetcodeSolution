#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-10 15:46
FileName: algorithm/P0284. 窥视迭代器.py
Description: 
"""


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.cur = self.iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.cur

    def next(self):
        """
        :rtype: int
        """
        t = self.cur
        self.cur = self.iterator.next() if self.iterator.hasNext() else None
        return t

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur is not None


if __name__ == '__main__':
    solution = PeekingIterator([1, 2, 3])
    print(solution.next())
    print(solution.peek())
    print(solution.next())
    print(solution.next())
    print(solution.hasNext())
