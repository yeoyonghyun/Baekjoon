while True:
    num = int(input())
    if num == 0:
        break
    else:
        palin = []
        for i in str(num):
            palin.append(i)
        palin2 = palin[:]
        palin2.reverse()
        if palin == palin2:
            print('yes')
        else:
            print('no')