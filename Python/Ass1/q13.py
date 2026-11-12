def tables(start, end):
    for i in range(start, end+1):
        if i % 2 != 0:
            print("\nTable of", i)
            for j in range(1, 11):
                print(i, "x", j, "=", i*j)
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
tables(start, end)