# given an integer return that integer reversed
# if the reversed integer is greater than (2^31)-1 or less than (-2^31) return 0


def reverse(x: int) -> int:
    upper_limit = (2**31)-1
    lower_limit = -(2**31)
    temp_string = ""
    
    number_to_reverse = str(x)
    for i in range(len(number_to_reverse)-1,-1,-1):
        # if number has a negative sign, add it to the beginning of the reversed number
        if number_to_reverse[i] != "-":
            temp_string = temp_string + number_to_reverse[i]
        else: 
            temp_string = "-" + temp_string 
            continue    
    reversed_number = int(temp_string)
    if (reversed_number > upper_limit) or (reversed_number < lower_limit):
        return 0
    else:
        return int(temp_string)

print(str(reverse(1534236469)))