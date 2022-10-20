
test = int(input())

def isprime(num):
    if num == 1:
        print('Not prime')
    elif num == 2:
        print('Prime')
    else:
        flag = 0
        for j in range(2, int(num**0.5)+1):
            if num % j == 0:
                flag = 0
                break
            else:
                flag = 1
        if flag == 0:
            print('Not prime')
        else:
            print('Prime')   
    
for t in range(test):
    num = int(input())
    isprime(num)
    
