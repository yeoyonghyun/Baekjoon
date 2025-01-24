# a = 100
# b = 99
# v = 1000000000


a,b,v = list(map(int, input().split()))



n = ((v-a)/(a-b))+1
if n == int(n):
    print(int(n))
else:
    print(int(n)+1)



# while True:
#     if a+(n*(a-b)) >= v:
#         print(n+1)
#         break
#     else:
#         n += 1