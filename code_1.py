# code for prime number

# def is_prime(num):
#     if num<2:
#         return False
#     for i in range(2,int(num**0.5)+1):
#         if num%i==0:
#             return False
#     return True
# num=int(input('Enter the number'))
# if is_prime(num):
#     print(f'{num} is a prime number')
# else:
#     print(f'{num} is not a prime number')


# code for factorial number

# num = int(input('enter the number'))

# def fact(num):
#   facto=1
#   for i in range(1,num+1):
#     facto=facto*i
#   print('fact is ',facto)
# fact(num)


# memo={}
# def fact(n):
#     if n==0:
#       return 1
#     if n in memo:
#        return memo[n]
#     memo[n]=n*fact(n-1)
#     return memo[n]
# print(fact(int(input('enter the number'))))

# import random

# num = random.sample(range(1,100),3)
# print(num)