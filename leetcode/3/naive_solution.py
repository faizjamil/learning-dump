def lengthOfLongestSubstring(s: str) -> int:
        # two for loops
        ans = 0
        for index_1 in range(0, len(s)-1):
            for index_2 in range(index_1+1, len(s)):
                if all_unique(s, index_1, index_2):
                    ans = max(ans, index_2 - 1)

        return ans

def all_unique(substring: str, start: int, end: int):
        # use set and store characters in string
        char_set = set([])
        for index in range(start, end):
            if char_set.__contains__(substring[index]):
                return False
            return True

# correct output: 3
print(lengthOfLongestSubstring("pwwkew"))
# correct output: 5
print(lengthOfLongestSubstring("ckilbkd"))
# correct output: 2
print(lengthOfLongestSubstring("aab"))
# correct output: 1
print(lengthOfLongestSubstring(" "))
# correct output: 2
print(lengthOfLongestSubstring("au"))
# correct output: 3
print(lengthOfLongestSubstring("dvdf"))
# correct output: 5
print(lengthOfLongestSubstring("anviaj"))
# correct output: 6
print(lengthOfLongestSubstring("asjrgapa"))
# correct output: 4
# string is 8 characters with both halves being the longest possible substring
# if the string has an even number of characters and we are in the middle
# check to see if the next character is a duplicate

print(lengthOfLongestSubstring("jbpnbwwd"))
# correct output: 6
print(lengthOfLongestSubstring("ohvhjdml"))