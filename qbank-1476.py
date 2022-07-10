# 문제은행 1476 - 날짜 계산

while True:
    E, S, M = input("준규 나라의 날짜를 입력하시오 ex) 1 1 1\n입력 -> ").split()
    count = 1
    copy_e =1
    copy_s = 1
    copy_m = 1
    
    if int(E) > 15 or int(S) > 28 or int(M) > 19:
        print("잘못 입력하셨습니다.")
        continue
    
    while True:
        if copy_e == int(E) and copy_s == int(S) and copy_m == int(M):
            break
        else:
            if copy_e == 15:
                if copy_s == 28:
                    copy_s = 1
                    if copy_m == 19:
                        copy_m = 1
                    else:
                        copy_m += 1
                elif copy_m == 19:
                    copy_m = 1
                    copy_s += 1
                else:
                    copy_m += 1
                    copy_s += 1
                copy_e = 1
                count += 1
            elif copy_s == 28:
                if copy_m == 19:
                    copy_m = 1
                else:
                    copy_m += 1
                copy_s = 1
                copy_e += 1
                count += 1
            elif copy_m == 19:
                copy_m = 1
                copy_e += 1
                copy_s += 1
                count += 1
            else:
                copy_e += 1
                copy_s += 1
                copy_m += 1
            
                count += 1
            
            
    print("준규가 사는 나라는 %d 연도입니다." % count)