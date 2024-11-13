#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2024-11-13 21:37
FileName: P0929. 独特的电子邮件地址
Description:
"""
from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '').split('+')[0]
            seen.add(f'{local}@{domain}')
        return len(seen)


if __name__ == '__main__':
    solution = Solution().numUniqueEmails(emails=["test.email+alex@leetcode.com",
                                                  "test.e.mail+bob.cathy@leetcode.com",
                                                  "testemail+david@lee.tcode.com"])
    print(solution)
