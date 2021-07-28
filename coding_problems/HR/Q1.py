# interview question for unnamed company
# two signals being generated
# whenever the signals are equal, freq is noted
# record maintain for the max simultaneous frequency this far
# each time a higher simul freq is noted, a var maxequal is updated
# both signals start at time = 0
# durations may be different, check if equal is performed until end of shorter signal
# if both signals have equal frequencies at a given time which is less than maxequal, maxequal stays the same
# Complete the 'updateTimes' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY signalOne
#  2. INTEGER_ARRAY signalTwo
#

def updateTimes(signalOne, signalTwo):
    max_equal = 0
    # to reduce time complexity we can use a hash map, add all elements from both arrays as keys, making note of the index those keys are at
    signal_elements = {}
    for k in range(0, len(signalOne)):
        #key will be a unique element among both arrays, value will be an array containing the indexes where each key is stored among the two arrays
        #two dictionaries might also work for this purpose
        if signalOne[k] in signal_elements:
            signal_elements[k].append(k)
        else:
            index = [k]
            signal_elements[k] = index
    # add the elements of signalTwo to dictionary, but offset the index by * 100 when adding
    for l in range(0, len(signalTwo)):
        if signalTwo[l] in signal_elements:
            signal_elements[l].append(l*100)
        else:
            index = [l*100]
            signal_elements[l] = index
    
    # naive solution is to check when one lement of one array equals another
    # in order words, if element i in signal one equals element j in signal two and i == j, then we increment one to max_equal
    # time complexity is O(n^2)
    # for i in range(0,len(signalOne)):
    #     for j in range(0, len(signalTwo)):
    #         if signalOne[i] == signalTwo[j] and i == j and current_max < signalOne[i]:
    #             current_max = max(current_max, signalOne[i])
    #             max_equal +=1

    return max_equal
signalOne = [3,3,10,20,5]
# signalOne = [1,2,3,4,1]
signalTwo = [4,7,11,20,6]
# signalTwo = [5,4,3,4,1]

print(updateTimes(signalOne, signalTwo))
# expected output should be 2