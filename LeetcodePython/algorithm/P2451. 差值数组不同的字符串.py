#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-02-02 11:42
FileName: P2451. 差值数组不同的字符串
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def oddString(self, words: List[str]) -> str:
        def process(word):
            nums = []
            for i in range(1, len(word)):
                nums.append(ord(word[i]) - ord(word[i - 1]))
            return tuple(nums)

        dic = defaultdict(list)
        for word in words:
            dic[process(word)].append(word)
        for v in dic.values():
            if len(v) == 1:
                return v[0]
        return 'error'


if __name__ == '__main__':
    solution = Solution().oddString(words=["adc", "wzy", "abc"])
    ic(solution)
