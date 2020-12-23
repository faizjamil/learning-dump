def lengthOfLongestSubstring(s: str) -> int:
    # create a record of the count of each letter
    # use a table of some sort, where each key is a letter and the value is the number of times that letter appears in s
    longest_substring = ""
    alphabet_characters = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
        ' ': 0
    }
    # iterate through each character of s
    # concat each character to a string and return length of string
    # only works for substrings at beginning of string
    # how to account for substrings elsewhere
    # perhaps lookahead to next letter and see if it is not a duplicate
    # if it is not duplicate, then reset count of all letters
    for index in range(0, len(s)):
        if s == "":
            break
        elif alphabet_characters[s[index]] < 1:
            longest_substring = longest_substring + s[index]
            alphabet_characters[s[index]] = alphabet_characters[s[index]] + 1
        elif s[index - 1].__eq__(s[index]):
            longest_substring = ""
            for key, value in alphabet_characters.items():
                alphabet_characters[key] = 0
        else:
            break
    return len(longest_substring)

print(lengthOfLongestSubstring("pwwkew"))