# link: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# q is an array representing the final arrangement of people in the line
# in other words, an unsorted array
# we can assume the initial array is sorted
# we essentially have to sort this array and find the minimum number of swaps in order to do that
# since when person n bribes another person o, o and n switch positions
# n can only swap positions with the person in front of them
# n can only switch positions twice
# if an element has moved more than two indecies, we cannot achieve the input state
# solution is explained here: https://www.youtube.com/watch?v=VT-ChOqUsBM
# we have two cases, bribe and no bribe
# to check to see if a person has been bribed, we check if that element belongs in that index
def minimumBribes(q):
    counter = 0
    for i in range(len(q)-1,0,-1  ):
        if q[i] != i+1:
            
            if q[i-1] == i + 1:
                counter += 1
                q[i],q[i-1] = q[i-1],q[i]
            elif q[i-2] == i+1:
                counter += 2
                temp = q[i-1]
                # swap q[i-1] and q[i-2]                
                q[i-1] = q[i-2]
                q[i-2] = temp 
                
                # swap q[i] and q[i-1]
                temp = q[i]
                q[i] = q[i-1]
                q[i-1] = temp
                
            else:
                print("Too chaotic")
                return
        
    print(counter)
# let i + 1 be the element that's supposed to be at q[i]
# if q[i] == i + 1
#   pass, we don't care about this
# else
#   if the previous element q[i-1] == i + 1 or in other words, if an element has been swapped one index back
#       this is the first bribe
#       add one to ccounter
#       swap the element at i-1 with the element at i
#   else if the element two indices back, q[i-2] == i + 1
#       increase counter by 2
#       swap q[i] and q[i-1]
#       swap q[i-1] and q[i-2]
#   else
#       
#       print("Too chaotic")
#       return
# THE CODE BELOW IS INCORRECT
# def minimumBribes(q):
#     min_number_of_swaps = 0
#     # need to keep track of how many times each element swaps
#     # if it exceeds two, we print "too chaotic"
#     # we do not need to compare to pre-generated array
#     # we can just check to see if an element is at the index [element-1]
#     # if not, then we need to swap it and keep track of the number of swaps
#     # once it is in the correct index, we reset the counter for the number of swaps
#     # perhaps we can subtract the indexes of where an element is in the final state from where it is supposed to be in a sorted array
#     # we can do something like
#     # for element in array
#     # see if it is at the index it normally is in a sorted array
#     # to do this, we simply check if the index + 1 equals the current element
#     # if not, then perhaps we can subtract the index it is supposed to be at versus the index it is at in the final state
#     # that gives us the amount of times an element has been swapped
#     # we get the index it is supposed to be at by taking the element and subtracting one
#     # if this algorithm is completly incorrect, then ¯\_(ツ)_/¯
#     for i in range(0, len(q)):
#         if q[i] != (i+1):
#             # then we have an element not in the correct place in the array
#             if ((q[i]-1) - i) < 1:
#                 continue
#             elif ((q[i]-1) - i) > 2:
#                 print("Too chaotic")
#                 return
#             else:
#                 min_number_of_swaps += ((q[i]-1) - i)

#     print(str(min_number_of_swaps))


# q = [5, 1, 2, 3, 7, 8, 6, 4]

# q= [1, 2, 5, 3, 7, 8, 6, 4]

q = [2, 1, 5, 3, 4]
# q = [2, 5, 1, 3, 4]
# q = [1,2,3,5,4,6,7,8] #1

# q = [4,1,2,3]
minimumBribes(q)