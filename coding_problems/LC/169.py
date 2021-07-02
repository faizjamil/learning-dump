# link: https://leetcode.com/problems/majority-element/

from typing import List
from utils import get_first_key_by_value
def majorityElement(nums: List[int]) -> int:
    # now i could do the naive approach first, or i can do the hashmap approach now
    elements = {}
    max_element_count = 0
    for i in range(0, len(nums)):
        if nums[i] in elements:
            # add one
            elements[nums[i]] = elements[nums[i]] + 1
        else:
            elements[nums[i]] = 1
    for value in elements.values():
        
        max_element_count = max(value, max_element_count)
    return get_first_key_by_value(elements, max_element_count)
nums = [3,2,3]
print(majorityElement(nums))
# expected output: 3