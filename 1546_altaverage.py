N = int(input())

scores = list(map(int,input().split()))

M = max(scores)

alt_average = []
for score in scores:
    alt_average.append(score/M*100)

average = (sum(alt_average))/N

print(average)