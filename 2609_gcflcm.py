# a, b = map(int, input().split())

# factors_a = []
# factors_b = []

# for i in range(1,a+1):
#     if a%i==0:
#         factors_a.append(i)

# for i in range(1,b+1):
#     if b%i==0:
#         factors_b.append(i)

# comm_factors = []
# for i in factors_a:
#     for j in factors_b:
#         if i ==  j:
#             comm_factors.append(i)
# max_factor = max(set(comm_factors))
# min_bae = int(a*b/max_factor)

# print(max_factor)
# print(min_bae)


num = list(map(int, input().split()))

facts = []
mult = 1

for n in num:
    for i in range(1, n+1):
        if n % i == 0:
            facts.append(i)
    mult *= n
for i in facts:
    if facts.count(i) == 2:
        gcf = i
        if gcf < i:
            gcf = i
lcm = int(mult/(gcf**(len(num)-1)))

print(f'{gcf}\n{lcm}')
