#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 09:57
FileName: P0451. 根据字符出现频率排序
Description:
"""

from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        return ''.join(sorted(list(s), key=lambda el: (counter.get(el), el), reverse=True))


if __name__ == '__main__':
    solution = Solution().frequencySort('tree')
    print(solution)
