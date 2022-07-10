# 문제은행 2480 - 주사위 3개로 돈 벌기

while True:
    a, b, c = input("주사위 눈을 3개 입력하시오.\n입력 -> ").split()
    
    
    if a == b == c:
        print("%d원" % (10000 + int(a)*1000))
    elif a == b or a == c:
        print("%d원" % (1000 + int(a) * 100))
    elif b == c:
        print("%d원" % (1000 + int(b) * 100))
    else:
        if int(a) > int(b) and int(a) > int(c):
            print("%d원" % (100 * int(a)))
        elif int(b) > int(c):
            print("%d원" % (100 * int(b)))
        else:
            print("%d원" % (100 * int(c)))