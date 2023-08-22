def fibonacci(num):
    if num<3: #first two value is equal to one 
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(9))

'''''
output is :
34

'''''
