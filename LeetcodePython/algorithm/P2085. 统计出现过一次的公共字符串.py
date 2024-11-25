#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-25 22:57
FileName: P2085. 统计出现过一次的公共字符串
Description:
"""
from typing import List
from collections import defaultdict


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cnt1, cnt2 = defaultdict(int), defaultdict(int)
        for word in words1:
            cnt1[word] += 1
        for word in words2:
            cnt2[word] += 1
        cnt = 0
        for k, v in cnt1.items():
            if v == 1 and cnt2.get(k, 0) == 1:
                cnt += 1
        return cnt


if __name__ == '__main__':
    solution = Solution().countWords(
        words1=["leetcode", "is", "amazing", "as", "is"], words2=["amazing", "leetcode", "is"])
    print(solution)
