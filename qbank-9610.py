# 문제은행 9610 - 사분면

while True:
    user_in = int(input("몇 개의 좌표?\n입력 -> "))
    
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q4 = 0
    AXIS = 0
    
    for i in range(user_in):
        a, b = input("좌표 -> ").split()
        if a == "0" or b == "0":
            AXIS += 1
        elif int(a) > 0 and int(b) > 0:
            Q1 += 1
        elif int(a) < 0 and int(b) > 0:
            Q2 += 1
        elif int(a) < 0 and int(b) < 0:
            Q3 += 1
        else:
            Q4 += 1
            
    print("Q1 : %d\nQ2 : %d\nQ3 : %d\nQ4 : %d\nAXIS : %d" % (Q1, Q2, Q3, Q4, AXIS))