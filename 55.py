'''
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl
restore(short), which expands the shortened string into the original url
If no such shortened string exists, return null
Hint: What if we enter the same URL twice?
'''

from random import choices
from pprint import pprint


class URLShortener:
    def __init__(self):
        self.shortToUrl = {}
        self.UrlToShort = {}
        charset = set(
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        )

    def shorten(self, url):
        if url in self.UrlToShort:
            return self.UrlToShort[url]
        short = ''.join(choices(population=url, k=6))
        while short in self.shortToUrl:
            short = ''.join(choices(population=url, k=6))
        self.shortToUrl[short] = url
        self.UrlToShort[url] = short
        return short

    def restore(self, short):
        if not self.shortToUrl[short]:
            return 'Not Found'
        return self.shortToUrl[short]


# Driver code
testcases = [
    'http://www.wikipedia.org',
    'http://www.stackoverflow.com',
    'http://www.geeksforgeeks.org',
    'http://developer.mozilla.org',
    'http://www.github.com',
    'http://www.hackerrank.com',
]

shortenedUrls = []

myUrlShortener = URLShortener()
for url in testcases:
    s = myUrlShortener.shorten(url)
pprint(myUrlShortener.shortToUrl)
print('\n\n')
pprint(myUrlShortener.UrlToShort)
