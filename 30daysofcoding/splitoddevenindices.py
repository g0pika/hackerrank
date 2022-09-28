N = int(input())
tmp1 = ""
tmp2 = ""
for i in range(0, N):
    S = input()
    for j in range(0, len(S)):
        if j % 2 == 0:
            tmp1 += S[j]
        else:
            tmp2 += S[j]
    print(f"{tmp1} {tmp2}")
    tmp1 = ""
    tmp2 = ""
