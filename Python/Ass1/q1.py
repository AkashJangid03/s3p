# Write a program to determine all the Pythagorean triplets in the range of 100 to 1000. 
# A Pythagorean triplet is a set of three integers i, j, k such that (i^2 + j^2 = k^2). 

for i in range (100, 1001): 
    for j in range (i+1, 1001):
        for k in range (j+1, 1001):
            if i*i + j*j == k*k:
                print(i, j, k)