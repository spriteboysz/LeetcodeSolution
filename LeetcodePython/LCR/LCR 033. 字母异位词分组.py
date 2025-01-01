#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-01 10:06
FileName: LCR 033. 字母异位词分组
Description:
"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[tuple(sorted(list(s)))].append(s)
        return list(dic.values())

if __name__ == '__main__':
    solution = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(solution)