# link: https://leetcode.com/problems/longest-common-prefix/
# given an array of strings, find the shortest common prefix
# use a loop to iterate thru elements
# naive solution is to use two for loops
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    shortest_Length = min(len(ele) for ele in strs)
    is_common_prefix = True
    j = 0
    common_prefix = ""
    while (j<shortest_Length):
        # check element at i in each array
        # we check the letter at index j in each element of the array
        # if there is any occurance where strs[i][j] that does not match the last letter inserted in the common prefix
        for i in range (0, len(strs)):
            if (i == 0):
                common_prefix = common_prefix + strs[i][j]   
            elif (strs[i][j] in common_prefix[j]):
                
                is_common_prefix = True
            else:
                is_common_prefix= False
                break
        if (is_common_prefix == False):
            common_prefix = common_prefix[:-1]
            break
        j += 1
    return common_prefix

# strs = ["dog","racecar","car"]   
# strs = ["flower","flow","flight"]   
# strs = ["cir", "car"]   
# strs = ["c","acc","ccc"]
strs = ["abca","aba","aaab"]
print(longestCommonPrefix(strs))
# java solution using a vertical scanning approach (what i appear to have used)
# public String longestCommonPrefix(String[] strs) {
#     if (strs.length == 0) return "";
#     String prefix = strs[0];
#     for (int i = 1; i < strs.length; i++)
#         while (strs[i].indexOf(prefix) != 0) {
#             prefix = prefix.substring(0, prefix.length() - 1);
#             if (prefix.isEmpty()) return "";
#         }        
#     return prefix;
# }
