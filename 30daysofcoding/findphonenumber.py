
n = int(input())

dict = {}

for i in range(n):
    text = input().split()
    dict[text[0]] = text[1]

while True:
    try:
        name = input()
        if name in dict:
            print(f"{name}={dict[name]}")
        else:
            print("Not found")
    except EOFError:
        break
