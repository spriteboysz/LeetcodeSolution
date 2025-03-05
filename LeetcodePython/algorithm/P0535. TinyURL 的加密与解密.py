#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-03-05 22:02
FileName: algorithm/P0535. TinyURL 的加密与解密.py
Description: 
"""

from icecream import ic


class Codec:
    urls = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.urls:
            index = self.urls.index(longUrl)
        else:
            self.urls.append(longUrl)
            index = len(self.urls) - 1
        return f'http://{index}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return f'{self.urls[int(shortUrl[7:])]}'


if __name__ == '__main__':
    url = "https://leetcode.com/problems/design-tinyurl"
    solution = Codec()
    ans = solution.decode(solution.encode(url))
    ic(ans)
