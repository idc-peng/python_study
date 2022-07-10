# 문제 50 각 자리 수를 출력

def div(num) :
    count = 0
    for i in range(1, num + 1) :
        if num % i == 0 :
            print(i)
            count += 1
    print()
    print(num, '의 약수의 개수 :', count)

user = int(input('정수를 입력하시오: '))
div(user)