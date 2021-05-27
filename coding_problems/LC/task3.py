# road consisting of N segments
# character S[K] may include either an "." or an "X"
# "X" represents a pothole
# this is not the correct solution

import math
#test_case_1 = ".X..X"
# test_case_1 = "X.XXXXX.X."
# test_case_1 = "XX.XXX.."
test_case_1 = "XXXX"
number_of_potholes = 0
number_of_good_spots = 0
amount_of_potholes = 0
in_pothole = False
for i in range(0, len(test_case_1)):
    string_to_check = test_case_1[i:i+2]
    if test_case_1[i] == "X":
        number_of_potholes +=1
    if test_case_1[i] == ".":
        number_of_good_spots+=1
    if (string_to_check == "XX" or string_to_check == ".X" or string_to_check == "X."):
        in_pothole = True
    if (string_to_check == ".."):
        in_pothole = False
        continue
    if (string_to_check == "X." and i == 0):
        amount_of_potholes+=1
        continue
    if (string_to_check == ".X" and i == len(test_case_1)-2):
        amount_of_potholes+=1
        continue
    if (string_to_check == "X." and in_pothole):
        amount_of_potholes+=1
        continue
if (number_of_good_spots == len(test_case_1)):
    amount_of_potholes = 0
if (number_of_potholes == len(test_case_1)):
    amount_of_potholes = math.ceil(float(number_of_potholes)/3.0)
print(amount_of_potholes)
    
