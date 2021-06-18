def solution(A):
    # write your code in Python 3.6
    # use sliding window method
    # we create a list to store all sums of all digits
    # we create the window, contains first two digits of array
    # no, that will not work, would only work if we were restricted to consecutive elements
    # naive approach
    # use two for loops to find all possible sums, add to array to contain the sums, then check the array to see if there are any sums that are equal
    # ooh boy, double nested for loops
    # there's maybe a way to do this recursively, but i'm not quite sure right now
    sums = []
    for i in range(0, len(A)):
        for j in range(0, len(A)):
            sums.append(A[i] + A[j])

    # i would use something like iters, but it seems to not affect the runtime that much if at 
    for k in range(0, len(sums)):
        for l in range(0, len(sums)):
            if sums[k] == sums[l]:
                return sums[k]
            else:
                return -1
A = [51,71,17,42]
# A = [51,71,17,42]
# A = [51,71,17,42]
# A = [51,71,17,42]
print(solution(A))