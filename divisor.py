# 약수 구하기 (divisor)

def div(num):
    count = 0                                           # 약수의 개수
    for i in range(1, num+1):                           # num + 1을 하여 자기 자신도 약수로 포함하였습니다.
        if num % i == 0:                                # 약수는 나눈 나머지가 0인 수 이므로 0이 나올 경우 출력을 하고 count + 1을 하여 약수의 개수를 계산하였습니다.
            if i == num :
                print(i)
                count += 1
            else :
                print(i, end = ", ")
                count += 1
            
    return count
    
while True:
    try:
        user_num = input("양의 정수를 입력하십시오. (범위는 0이상 300 이하)\n입력란 -> ") # 값을 숫자열이 아닌 문자열로 입력 받아 enter를 입력할 시 종료되도록 구성하였습니다.
        if user_num == "":                              # 엔터를 입력할 시 프로그램 종료
            print("-" * 25)
            print("프로그램이 종료되었습니다.")
            break
        elif 0 <= int(user_num) <= 300 :
            print()
            print("-" * 25)
            print("입력 값", user_num, "의 약수\n->", end = " ")     # 약수가 개행이 되면서 출력되면 출력값이 밑으로 나오게 되어 가독성이 떨어지므로 end = " " 를 이용하여 띄어쓰기로 하였습니다.
            count_num = div(int(user_num))
            print(user_num, "의 약수의 총 개수는 ->", count_num, "개")             # 약수의 개수 출력
            print("-" * 25)
        else :
            print("-" * 25)
            print("범위 밖의 숫자입니다.\n처음부터 다시 시작합니다.")
            print("-" * 25)
    except ValueError:                                  # ValueError를 통해 양의 정수가 아닌 실수나 문자열이 입력됬을 경우 예외처리를 하였습니다.
        print("-" * 25)
        print("양의 정수가 아닌 문자나 숫자가 입력되었습니다.\n처음부터 다시 시작합니다.")
        print("-" * 25)