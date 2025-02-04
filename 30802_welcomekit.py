N = int(input())
num = list(map(int, input().split()))
T, P = map(int, input().split())

T_group = 0
for i in num:
    if i%T == 0:
        T_group += i//T
    else:
        T_group += i//T + 1

print(T_group)
print(N//P, N%P)