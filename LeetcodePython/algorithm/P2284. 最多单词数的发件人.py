#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-01-04 21:43
FileName: P2284. 最多单词数的发件人
Description:
"""
from collections import defaultdict
from typing import List

from icecream import ic


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        dic = defaultdict(int)
        for message, sender in zip(messages, senders):
            dic[sender] += len(message.strip().split())
        ic(dic)
        return max(dic, key=(lambda el: (dic[el], el)))


if __name__ == '__main__':
    solution = Solution().largestWordCount(
        messages=["Hello userTwooo", "Hi userThree", "Wonderful day Alice", ""],
        senders=["Alice", "userTwo", "userThree", "Alice"])
    ic(solution)
