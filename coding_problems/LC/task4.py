# find the minimum number of elements that need to be flipped to have an alternating sequence of 1s and 0s

#test_case1 = [1,0,1,0,1,1]  - one flip
#test_case1 = [1,1,0,1,1] - two flips
# test_case1 = [0,1,0] - zero flips
# test_case1 = [0,1,1,0] - two flips
test_case1 = [0,1,1,0,1,0,1,1,1,1]

min_number_of_flips = 0
sliced_array = test_case1[:]

# if there is a 0,1,1,0 in middle of array, then go to for loop
# then wherever there is the sequence 0,1,1, delete that from the array
k = 0
while (k < len(test_case1)):
    test = test_case1[:4]
    
    if [0,1,1,0] == test_case1[:4]:
        min_number_of_flips +=2
        if (len(sliced_array) >= 4):
            sliced_array.remove(0)
            test_case1.remove(0)
            sliced_array.remove(1)
            test_case1.remove(1)
            sliced_array.remove(1)
            test_case1.remove(1)
            sliced_array.remove(0)
            test_case1.remove(0)
            continue
    elif [1,1,1,1] == test_case1[:4]:
        min_number_of_flips +=2
        if (len(sliced_array) >= 4):
            sliced_array.remove(1)
            test_case1.remove(1)
            sliced_array.remove(1)
            test_case1.remove(1)
            sliced_array.remove(1)
            test_case1.remove(1)
            sliced_array.remove(1)
            test_case1.remove(1)
            continue
    else :
        test_case1.pop(0)
        k+=1

for i in range(0,len(sliced_array)-1):
    if sliced_array[i] == sliced_array[i+1]:
         min_number_of_flips +=1
print(min_number_of_flips)