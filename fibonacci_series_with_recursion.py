# def fibonacci(n):
#     if n==0 or n==1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)


# if __name__ == '__main__':
#     print(fibonacci(4))


# # 0,1,1,2,3


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))