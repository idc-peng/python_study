# 문제은행 2523 - 별 찍기(늘어나다 줄어드는 모양)

while True:
    user_in = int(input("몇 개의 별이 보이십니까?\n절대 문자 입력 금지\n입력 -> "))
    
    for x in range(1, int(user_in)*2):
        if x > int(user_in):
            for i in range((int(user_in) - (x - int(user_in)))):
                print("*", end = "")
        else:
            for i in range(x):
                print("*", end = "")
        print()
    print("-" * 40)