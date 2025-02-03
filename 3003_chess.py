

# k, q, l, b, kn, p  = map(int,input().split())



# k = 1 - k
# q = 1 - q
# l = 2 - l
# b = 2 - b
# kn = 2 - kn 
# p = 8 - p

# chess = k, q, l, b, kn, p

# ans = ""
# for n in chess:
#     ans = ans + str(n) + " "

# print(ans)




k, q, l, b, kn, p  = map(int,input().split())

k = 1 - k
q = 1 - q
l = 2 - l
b = 2 - b
kn = 2 - kn 
p = 8 - p

chess = k, q, l, b, kn, p

print(*chess)
