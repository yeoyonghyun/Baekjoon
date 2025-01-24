

while True :
    a, b, c = map(int, input().split())
    hyp = max(a,b,c)
    sec = a**2 + b**2 + c**2
    if sec == 0:
        break
    if hyp**2 == sec-(hyp**2):
        print("right")
    else:
        print("wrong")