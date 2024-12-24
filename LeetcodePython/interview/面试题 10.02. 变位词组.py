#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-23 22:50
FileName: 面试题 10.02. 变位词组
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)
        return list(map(lambda el: list(el), dic.values()))


if __name__ == '__main__':
    solution = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(solution)
