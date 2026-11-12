count = 0
num = 2
total = 0
while count < 10: 
    isPrime = True
    for i in range (2, num): 
        if num % i == 0: 
            isPrime =  False
            break
    if isPrime: 
        total += num 
        count += 1
    num = num + 1
print("Sum of first 10 prime numbers: ", total)