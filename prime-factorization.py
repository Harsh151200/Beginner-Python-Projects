"""
Prime Factorization -
Have the user enter a number and find all Prime Factors
(if there are any) and display them.
"""

num = int(input("Enter a number : "))

if num == 1:
    print("It has only prime factor i.e 1")
elif num < 1:
    print("Invalid number. It must be 1 or greater than 1")
else:
    print(f'Prime Factors of {num} are  :  ',end = " ")
    print("1",end = " ")
    while(num):
        for i in range(2, num+1):
            if num % i == 0:
                print(f"x {i} ", end=(" "))
                break
        num = int(num/i)
print('\n')