# link: https://www.hackerrank.com/challenges/sparse-arrays/problem
# optimized solution: https://youtu.be/BZdnvTBO4vI
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
# naive approach
# we want to check each element of the strings array with each element of the queries array
# for every string in strings
#   check if each element in query matches element in string
#   if yes, add one to counter


def matchingStrings(strings, queries):
    matching = []
    for i in range(0,len(queries)):
        matching_count = 0
        for j in range(0,len(strings)):
            if queries[i] == strings[j]:
                matching_count +=1
        matching.append(matching_count)

    return matching

# expected output: [2, 1, 0]
# strings = ['ab', 'ab', 'abc']
# queries = ['ab','abc','bc']

# expected output: [2, 1, 0]
# strings = ['aba', 'baba', 'aba', 'xzxb']
# queries = ['aba','xzxb','ab']
# expected output: [1, 0, 1]

strings = ['def', 'de', 'fgh']
queries = ['de','lmn','fgh']
print(matchingStrings(strings, queries))
