def factorial(n):
    result = 1
    for i in range(1, n + 1): # for number in range(n, 0, -1):
        result *= i
    return result 

    # while n > 0:
    #     result *= n
    #     n -= 1


number = int(input('Enter a positive integer: '))
print(factorial(number))