# Add 1 to each digit of a number 
def add1(n): 
    res = 0
    place = 1
    while n > 0:
        digit = n%10
        digit = (digit+1)%10
        res = res + digit * place
        place = place * 10
        n //= 10
    print(res)
n = int(input("Enter a number: "))
add1(n)