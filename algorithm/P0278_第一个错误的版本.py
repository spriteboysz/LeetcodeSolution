#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-07 22:26:11
LastEditTime: 2022-02-03 21:56:01
Description: 
FilePath: 278.第一个错误的版本.py
'''
#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return right

# @lc code=end
