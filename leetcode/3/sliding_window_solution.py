from os import remove


def lengthOfLongestSubstring(s: str) -> int:
    # two for loops
    
    ans = 0
    length = len(s)    
    window_start = 0
    window_end = 0
    char_set = set([])
    # for loop, figure out violating condition
    # violating condition would be if the current letter is already in the running string
    # check letter at window_end
    # if that is in string, then move window one space over
    # else, increase the window size (increase window_end)
    
    while (window_start < length and window_end < length):
        if (not(char_set.__contains__(s[window_end]))):
            char_set.add(s[window_end])
            window_end += 1
            ans = max(ans, window_end - window_start)
        else:
            char_set.remove(s[window_start])
            window_start += 1

    return ans

def all_unique(substring: str, start: int, end: int):
        # use set and store characters in string
        char_set = set([])
        for index in range(start, end):
            ch = substring[index]
            if char_set.__contains__(ch):
                return False
            char_set.add(ch)

        return True

# correct output: 3
#print(lengthOfLongestSubstring("pwwkew"))
# correct output: 5
# print(lengthOfLongestSubstring("ckilbkd"))
# correct output: 2
# print(lengthOfLongestSubstring("aab"))
# correct output: 1
# print(lengthOfLongestSubstring(" "))
# correct output: 2
# print(lengthOfLongestSubstring("au"))
# correct output: 3
# print(lengthOfLongestSubstring("dvdf"))
# correct output: 5
# print(lengthOfLongestSubstring("anviaj"))
# correct output: 6
# print(lengthOfLongestSubstring("asjrgapa"))
# correct output: 4
# string is 8 characters with both halves being the longest possible substring
# if the string has an even number of characters and we are in the middle
# check to see if the next character is a duplicate

# print(lengthOfLongestSubstring("jbpnbwwd"))
# correct output: 6
#print(lengthOfLongestSubstring("ohvhjdml"))
# correct output: some large number
print(lengthOfLongestSubstring())