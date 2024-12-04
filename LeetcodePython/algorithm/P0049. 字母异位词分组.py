#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-12-04 21:26
FileName: P0049. 字母异位词分组
Description:
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            group[''.join(sorted(list(s)))].append(s)
        return list(group.values())


if __name__ == '__main__':
    solution = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(solution)
