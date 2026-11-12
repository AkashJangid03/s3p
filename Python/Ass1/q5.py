n = int(input("Enter the number of values: "))
total = 0
for i in range (n):
    num = float(input("Enter number: "))
    total = total + num 
avg = total / n
print("Average: ", avg)
