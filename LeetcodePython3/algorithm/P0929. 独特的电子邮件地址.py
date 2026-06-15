#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-06-16 00:18
FileName: P0929. 独特的电子邮件地址.py
Description:
"""
from typing import List


class Solution:
    @staticmethod
    def process(email):
        local, domain = email.split('@')
        return local.replace('.', '').split('+')[0] + '@' + domain

    def numUniqueEmails(self, emails: List[str]) -> int:
        return len({self.process(email) for email in emails})


if __name__ == '__main__':
    solution = Solution().numUniqueEmails(
        emails=[
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"
        ])
    print(solution)
