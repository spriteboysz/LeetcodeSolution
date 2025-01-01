#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 10:09
FileName: LCR 034. 验证外星语词典
Description:
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {ch: i for i, ch in enumerate(order)}
        lst = [[index[ch] for ch in word] for word in words]
        return all(lst[i - 1] <= lst[i] for i in range(1, len(lst)))


if __name__ == '__main__':
    solution = Solution().isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
    print(solution)
