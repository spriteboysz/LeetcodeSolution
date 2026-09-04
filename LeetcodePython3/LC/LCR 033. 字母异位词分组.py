#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-09-03 21:11
FileName: LC/LCR 033. 字母异位词分组.py
Description: 
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[''.join(sorted(s))].append(s)
        return [v for v in dic.values()]


if __name__ == '__main__':
    solution = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(solution)
