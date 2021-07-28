# link: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# a left rotation shifts all elements of an array left one index
# the first element becomes the last element, all other elements get pushed one index to the left

# a is an array of integers

def rotLeft(a, d):
    # the easiest method is probably to take an array, pop the first element
    for i in range(0, d):
        temp = a.pop(0)
        a.append(temp)

    return a


print(rotLeft([1,2,3,4,5],4))