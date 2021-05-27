
def fib_sequence(num):
        fib_num = int(num)
        num_of_additions = fib_num
        fib_sequence = [0,1]
        fib_sum = 0
        current_fib_number = 0
        for i in range(1, num_of_additions):
            test1 = fib_sequence[i-1]
            test2 = fib_sequence[i]
            current_fib_number = (fib_sequence[i-1] + fib_sequence[i])
            
            fib_sequence.append(current_fib_number)
            fib_sum = current_fib_number
        return fib_sum
print(fib_sequence(5))
        