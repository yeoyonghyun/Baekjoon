N = int(input())
num = list(map(int, input().split()))
prime = []

for nu in num:
    factor = list(range(1, nu+1))
    for i in range(0, nu):
        factor[i] = nu%factor[i]
    if factor.count(0) == 2:
        prime.append(nu)
print(len(prime))