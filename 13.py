# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def longest_substr_k_distinct_characters(string, k):
    longest_substr_start_index = longest_substr_end_index = 0
    distinct_char_set = set()
    freq = [0]*26
    # left, right denote the boundry of sliding window
    left = 0
    for right in range(len(string)):
        ch = string[right]
        distinct_char_set.add(ch)
        freq[ord(ch) - 97] += 1
        
        while len(distinct_char_set) > k:
            ch = string[left]
            freq[ord(ch) - 97] -= 1
            if freq[ord(ch) - 97] == 0:
                distinct_char_set.remove(ch)
            left += 1
        
        if (longest_substr_end_index - longest_substr_start_index) < (right - left):
            longest_substr_end_index = right
            longest_substr_start_index = left
    return string[longest_substr_start_index: longest_substr_end_index + 1]


# Driver code
test_cases = {
    'abcba': 2,
    'abcbdbdbbdcdabd': 2,
    'aabcbdbdbbdcdabd': 3,
    'aabacbebebe': 3,
}

for key, val in test_cases.items():
    print(longest_substr_k_distinct_characters(key, val))