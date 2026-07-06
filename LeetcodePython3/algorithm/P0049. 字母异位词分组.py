#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-06 23:11
FileName: P0049. 字母异位词分组.py
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)
        return list(dic.values())


if __name__ == '__main__':
    solution = Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
    print(solution)
