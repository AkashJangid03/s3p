def triangle(n):
    for i in range (1, n+1):
        print(" " * (n-i), end="")
        for j in range(i):
            print("*", end=" ")
        print()
n = int(input("Enter the number of rows: "))
triangle(n)