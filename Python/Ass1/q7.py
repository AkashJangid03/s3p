def strongnum(start, end):
    for num in range(start, end+1):
        temp = num
        total = 0
        while temp > 0: 
            digit = temp % 10

            fact = 1
            for i in range (1, digit+1): 
                fact = fact * i

            total += fact
            temp //= 10

            if num == total: 
                print(num, end=" ")

start = int(input("Enter the starting element: "))
end = int(input("Enter the ending number: "))
strongnum(start, end)