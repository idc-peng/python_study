# 문제은행 1193 - 분수찾기

while True:
    user_in = input("몇 번째 분수를 찾으시겠습니까?\n입력 -> ")
    before_num = 0
    count = 0
    
    if user_in == "":
        print("프로그램을 종료합니다.")
        break
    
    for i in range(1, (int(user_in) + 1)):
        count += i
        if count >= int(user_in):
            if count == int(user_in):
                if i % 2 == 0:
                    print("%d/1" % i)
                    break
                else:
                    print("1/%d" % i)
                    break
            else:
                if i % 2 == 0:
                    print("%d/%d" % ((int(user_in) - count+i), (count+1 - int(user_in))))
                    break
                else:
                    print("%d/%d" % ((1+count - int(user_in)), (int(user_in) - count+i)))
                    break
        else:
            before_num = i