def factorial(n):
    
    if n == 0:
        return 1
    elif n>0:
        for x in range(n-1,0,-1):
            n=n*(x)
        return n
    else: 
        print('error')

# Get the number from the user
num = int(input("Enter a number: "))

# Calculate the factorial
result = factorial(num)

# Print the result
print('The factorial of',num,'is', result)