# link: link: https://www.hackerrank.com/challenges/2d-array/problem
# parameter: arr- an arbitrary 6 x 6 array
import sys
def hourglassSum(arr):
    if (len(arr) < 6 or arr == None):
        return 0
    else:
        sums = []
        # left_edge = 0
        # right_edge = 2
        for i in range(0, len(arr)-2):
            if len(arr[i]) < 6 :
                return 0
            for j in range(0, len(arr[i])-2):
                sums.append(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
        max_sum = sys.maxsize*(-1)
        for k in range(0, len(sums)):
            max_sum = max(max_sum, sums[k])
        
        return max_sum

# expected output is -19
# 0 -4 -6 0 -7 -6
# -1 -2 -6 -8 -3 -1
# -8 -4 -2 -8 -8 -6
# -3 -1 -2 -5 -7 -4
# -3 -5 -3 -6 -6 -6
# -3 -6 0 -8 -6 -7
# driver code
arr = [
    [0,-4,-6,0,-7,-6], 
    [-1,-2,-6,-8,-3,-1],
    [-8,-4,-2,-8,-8,-6],
    [-3,-1,-2,-5,-7,-4],
    [-3,-5,-3,-6,-6,-6],
    [-3,-6,0,-8,-6,-7]]
# arr = [
#     [1,1,1,0,0,0], 
#     [0,1,0,0,0,0],
#     [1,1,1,0,0,0],
#     [0,0,2,4,4,0],
#     [0,0,0,2,0,0],
#     [0,0,1,2,4,0]]
# arr = [
#     [-9, -9, -9, 1, 1, 1], 
#     [0, -9,  0,  4, 3, 2],
#     [-9, -9, -9,  1, 2, 3],
#     [0,  0,  8,  6, 6, 0],
#     [0,  0,  0, -2, 0, 0],
#     [0,  0,  1,  2, 4, 0]]
print(hourglassSum(arr))