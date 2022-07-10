# 계산기

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def remain(a, b):
    return a % b
    
def squ(a, b):
    c = a
    if b > 0:
        for i in range(b - 1):
            c = c * a
        return c
    elif b < 0:
        for i in range((-b) - 1):
            c = c * a
        return -c

while True:
    print("원하시는 사칙연산을 고르시오.")
    print("덧셈 - 1 / 뺄셈 - 2 / 곱셈 - 3 / 나눗셈 - 4 / 나눈 나머지 - 5 / 승 - 6")
    user_in = input()
    
    if user_in == "" :
       print("프로그램을 종료합니다.")
       break
       
    print("-" * 25)
    user_num1 = int(input("앞에 올 숫자를 입력하시오."))
    user_num2 = int(input("뒤에 올 숫자를 입력하시오."))
    
    if user_in == "1" :
        result = plus(user_num1, user_num2)
    elif user_in == "2":
        result = minus(user_num1, user_num2)
    elif user_in == "3":
        result = mult(user_num1, user_num2)
    elif user_in == "4":
        result = div(user_num1, user_num2)
    elif user_in == "5":
        result = remain(user_num1, user_num2)
    elif user_in == "6":
        result = squ(user_num1, user_num2)    
        if result < 0 :
            print("입력하신 값의 결과는 " , "1 /", -result , " 입니다.")
            print("-" * 25)
            print()
            continue
    else :
       print("계산기에 없는 계산입니다.")
       continue
    
    print("입력하신 값의 결과는 " , result , " 입니다.")
    print("-" * 25)
    print()
