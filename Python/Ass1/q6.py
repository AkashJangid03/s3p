def armstrong_number(start, end): 
    for i in range (start, end+1):
        order = len(str(i))
        temp = i 
        digit_sum = 0
        while temp > 0:
            digit = temp % 10
            digit_sum += digit ** order
            temp //= 10
        if i == digit_sum: 
            print(i, end=", ")
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
armstrong_number(start, end)