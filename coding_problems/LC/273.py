# link: https://leetcode.com/problems/integer-to-english-words/
# for when i want to challange myself (or mmake myself suffer)
from utils import get_first_key_by_value

MAX_VALUE = 2,147,483,647
numbers_to_values = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Eleven": 11,
    "Twelve": 12,
    "Thirteen": 13,
    "Fourteen": 14,
    "Fifteen": 15,
    "Sixteen": 16,
    "Seventeen": 17,
    "Eighteen": 18,
    "Nineteen": 19,
    "Twenty": 20,
    "Thirty": 30,
    "Fourty": 40,
    "Fifty": 50,
    "Sixty": 60,
    "Seventy": 70,
    "Eighty": 80,
    "Ninety": 90,
    "Hundred": 100,
    "Thousand": 1000,
    "Million": 1000000,
    "Billion": 1000000000
}
def numberToWords(num: int) -> str:
    # soo we wanna in this case start from the ones place value
    # after we pass the undreds place value we wanna look at the next three places if they exist
    # if so, then we multiply that by 10000
    # we do a similar thing for million
    pass
