def pattern(n): 
    for i in range (n):
        for j in range (n): 
            if i==n//2 and j==n//2: 
                print("@", end="")
            else:
                print("*", end="")
        print()
pattern(6)