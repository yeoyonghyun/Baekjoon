N, M = map(int, input().split())
num = list(map(int, input().split()))

nlist = []

for i in num:
    for j in num:
            for k in num:
                if not i==j and not j==k and not i==k:
                    sum = i+j+k
                    if sum <= M:
                        nlist.append(sum)
                        

print(max(set(nlist)))