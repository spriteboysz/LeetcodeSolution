#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 15:00
FileName: LC/LCR 160. 数据流中的中位数.py
Description: 
"""


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data = sorted(self.data)
        n = len(self.data)
        if n % 2 != 0:
            return self.data[int(n / 2)]
        return (self.data[int(n / 2)] + self.data[int(n / 2) - 1]) / 2


if __name__ == '__main__':
    median_finder = MedianFinder()
    median_finder.addNum(1)
    median_finder.addNum(2)
    print(median_finder.findMedian())
    median_finder.addNum(3)
    print(median_finder.findMedian())
