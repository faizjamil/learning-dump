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
            test = alphabet_characters[s[index]]
            if s == "":
                break
            # if we aren't at the end of string, if character is unique, concat it to longest_substring
            elif alphabet_characters[s[index]] < 1 and index < len(s):
                longest_substring = longest_substring + s[index]
                alphabet_characters[s[index]] = alphabet_characters[s[index]] + 1
            elif len(s) == 1:
                
                longest_substring = s

            # if the character is not unique and we are in the muddle of the string
            elif index < len(s) - 1 and index > 0:
                    duplicate_of_character_at_beginning_found = False
                    
                    # if the number of characters in the longest substring is larger
                    # than the number of characters left in the substring, we have found the longest substring
                    # if the first character has exactly one duplicate somewhere in the string
                    # skip the first character
                    # a hella naive solution
                    for char in range(0, len(s)):
                        if char > 0:
                            if s[0] == s[char]:
                                alphabet_characters[s[0]] = 0
                                longest_substring = longest_substring[1:]
                                longest_substring = longest_substring + s[char]
                                alphabet_characters[s[char]] = alphabet_characters[s[char]] + 1
                                duplicate_of_character_at_beginning_found = True
                                break
                            elif alphabet_characters[s[char]] == alphabet_characters[s[index]]:
                                break
                    if (len(longest_substring) > len(s) - index) and duplicate_of_character_at_beginning_found == False:
                        break
                    # if the previous character is the same as current character
                    # start new longest_substring
                    elif s[index - 1].__eq__(s[index]) and index < len(s):
                        longest_substring = s[index]
                        for key, value in alphabet_characters.items():
                            alphabet_characters[key] = 0
                        alphabet_characters[s[index]] = alphabet_characters[s[index]] + 1
                    # if we are in this conditional, assume that duplicate letter has been found
                    elif (len(longest_substring) == len(s) // 2) and (len(s) % 2 == 0) and duplicate_of_character_at_beginning_found == False:
                        break
                    
            elif len(s) == 2:
                if (s[0] == s[1]):
                    break
                else:
                    longest_substring = s
            elif index < len(s) - 1:
                if s[index - 1].__eq__(s[index]) or s[index + 1].__eq__(s[index]):
                    break
                elif alphabet_characters[s[index]] >=1 and alphabet_characters[s[index+1]] == 0:
                    alphabet_characters[s[index]] = 0
                    longest_substring = ""
            else:
                break
        return len(longest_substring)

# correct output: 3
# print(lengthOfLongestSubstring("pwwkew"))
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
print(lengthOfLongestSubstring("ohvhjdml"))