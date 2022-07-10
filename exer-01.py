# 정수 맞추기

import random                           # 랜덤모듈 사용

while True:                             # 무한루프로 게임을 하고자하면 무한히 할 수 있도록 구성했습니다.
    com_num = random.randrange(1,26)    # 1~25 사이의 정수를 랜덤으로 받습니다.
    count = 0                           # count는 몇 회 진행했는지를 확인합니다.
    
    for i in range(10):                 # 반복문을 2회 사용하여 break를 한 번 하는 경우에는 다시 게임이 진행됩니다.
        user_num = int(input("예상되는 숫자를 입력하세요 : "))
        count += 1
        if com_num == user_num:         # 정수를 맞춘 경우
            print("맞다.")
            print("-" * 25)
            print("축하합니다.", count, "번 만에 맞췄습니다.")
            user_in = input("게임을 다시 하시겠습니까? \n계속하시려면 '1'을 입력하시고 종료하시려면 '2'를 입력하세요.")
            if user_in == '1':
                break
            elif user_in == '2':        # 프로그램 종료 - 1
                break
        elif com_num > user_num:        # 작은 경우
            print("작다.")
        elif com_num < user_num:        # 큰 경우
            print("크다.")
    
    try:
        if user_in == '2':              # 프로그램 종료 - 2
            break
    except NameError:                   # 만약 10번 내에 못 맞췄을 경우 오류를 반환하지 않고 게임을 다시 시작합니다.
        print("아쉽습니다. \n10번 내에 맞추지 못 했습니다. 게임을 다시 진행합니다.")
        print("-" * 25)