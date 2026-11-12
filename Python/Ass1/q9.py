def num(n):
    count=0
    for i in range(1, n+1):
        if i%2!=0 and i%3!=0:
            print(i, end=" ")
            count += 1
    print("count: ", count)
n = int(input("Enter the number: "))
num(n)