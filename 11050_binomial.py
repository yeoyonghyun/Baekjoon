N, K = map(int, input().split())


def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(int(fact(N)/(fact(K)*fact(N-K))))