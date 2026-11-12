def series_sum(n): 
    total = 1
    fact = 1
    for i in range(2, n+1): 
        fact = fact * i
        total = total +1/fact
    print(total)
n = int(input("Enter a value: "))
series_sum(n)