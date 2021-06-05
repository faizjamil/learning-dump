# link: https://www.hackerrank.com/challenges/array-left-rotation/problem


# algorithm:
# for int i = 0; i <= number of left rotations; i++
#     for int j = 0; j < arr.length; j++
#          int last_element = arr[arr.length-1]
#          int first_element = arr[0]
#          arr[i] = arr[i+1]
#          arr.append(first_element)
#
#
# given two parameters, d and arr, return arr with d left rotations performed on it

def rotateLeft(d, arr):
    for i in range(0,d):
        first_element = arr[0]
        arr.pop(0)
        arr.append(first_element)
        # don't use this, time inefficient
        # instead, store the first element, pop it then add it to the end of the array
        # for j in range(0, len(arr)-1):
        #     arr[j] = arr[j+1]
        # arr[len(arr)-1]= first_element

    return arr

arr = [1,2,3,4,5]
print(rotateLeft(4, arr))