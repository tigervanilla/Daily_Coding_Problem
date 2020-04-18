# This problem was asked by Twitter.

# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
# return all strings in the set that have s as a prefix.

# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

class Node:
    def __init__(self):
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_word_end = True

    def get_all_words(self, node, string_till_now, words):
        if len(node.children) != 0:
            if node.is_word_end:
                words.append(string_till_now)
            for key, val in node.children.items():
                self.get_all_words(val, string_till_now + key, words)
        elif len(node.children) == 0 and len(string_till_now) > 0:
            words.append(string_till_now)

    def search(self, pattern):
        node = self.root
        pattern_copy, n = pattern, len(pattern)
        suggestions = []
        while n > 0:
            if pattern_copy[0] not in node.children:
                print('No Suggestions')
                break
            node = node.children[pattern_copy[0]]
            pattern_copy = pattern_copy[1:]
            n -= 1
        if n == 0:
            self.get_all_words(node, pattern, suggestions)
            print(suggestions)



# Driver code
ob = Trie()

ob.insert('ball')
ob.insert('bat')
ob.insert('deer')
ob.insert('deal')
ob.insert('doll')
ob.insert('dog')
ob.insert('dork')
ob.insert('do')
ob.insert('dorm')
ob.insert('send')
ob.insert('sense')

ob.search('de')
ob.search('do')
ob.search('sen')
ob.search('b')