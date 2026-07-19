#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2026-07-18 23:13
FileName: P0535. TinyURL 的加密与解密.py
Description:
"""


class Codec:
    urls = []

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.urls:
            self.urls.append(longUrl)
        index = self.urls.index(longUrl)
        return f'https://{index}'

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        index = int(shortUrl.split('/')[-1])
        return self.urls[index]


if __name__ == '__main__':
    codec = Codec()
    print(codec.decode(codec.encode('https://leetcode.com/problems/design-tinyurl')))
