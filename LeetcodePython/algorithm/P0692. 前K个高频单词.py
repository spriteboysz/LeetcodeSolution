#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-08 11:38
FileName: P092. 前K个高频单词
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = defaultdict(int)
        for word in words:
            dic[word] += 1
        return sorted(dic, key=lambda el: (-dic[el], el))[:k]


if __name__ == '__main__':
    solution = Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4)
    print(solution)
