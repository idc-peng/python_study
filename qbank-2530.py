# 문제은행 2530 - 인공지능 시계(덕고기 굽굽)

while True:
    hour, minu, sec = input("현재 시각을 입력하시오.\n입력 -> ").split()
    time = int(input("걸리는 시간을 입력하시오."))
    min_count = 0
    hour_count = 0
    
    a = int(hour)
    b = int(minu)
    c = int(sec)
    c += time
    
    while True:
        if c > 60:
            c -= 60
            min_count += 1
        b += min_count
        min_count = 0
        if b > 60:
            b -= 60
            hour_count += 1
        a += hour_count
        if a > 23:
            a -= 23
        
        if a <= 23 and b <= 60 and c <= 60:
            break
    print("%d시 %d분 %d초" % (a, b, c))