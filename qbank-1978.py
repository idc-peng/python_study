# 문제은행 1978 - 소수 찾기

while True:
    index = int(input("원하는 숫자의 개수를 입력하세요~\n입력 -> "))
    user_num = input("숫자 입력\n-> ").split()
    div_list = []
    count_list = []
    
    if index == len(user_num):
        for i in user_num:
            for x in range(1, (int(i) + 1)):
                if (int(i) % x) == 0:
                    div_list.append(x)
                else:
                    continue
            if len(div_list) == 2:
                count_list.append(i)
            div_list.clear()
    
        print("결과는 %d 개의 소수를 입력하셨군요." % len(count_list))
        div_list.clear()
        user_num.clear()
        count_list.clear()
    else:
        print("수량이 틀립니다~")