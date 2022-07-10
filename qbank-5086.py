# 문제은행 5086 - 배수와 약수

while True:
    try:
        user_a, user_b = input("약수와 배수관계를 알아보는 프로그램입니다.\n두 수를 입력하시오 -> ").split()
    
        a = int(user_a)
        b = int(user_b)
    
        if b % a == 0:
            if b == 0 or a == 0:
                print("neither")
            else:
                print("factor")
        elif a % b == 0:
            if a == 0 or b == 0:
                print("neither")
            else:
                print("multiple")
        else:
            print("neither")
    except ZeroDivisionError:
        print("neither")