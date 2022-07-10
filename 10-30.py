# 문제 30 각 자리 수를 출력

def num_position(num) :
    num_5 = num // 10000
    num_4 = (num // 1000) - (num_5 * 10)
    num_3 = (num // 100) - (num // 1000 * 10)
    num_2 = (num // 10) - (num // 100 * 10)
    num_1 = (num // 1) - (num // 10 * 10)
    
    print(num_5, ',', num_4, ',', num_3, ',', num_2, ',', num_1)


user = int(input('다섯 자리 숫자를 입력하시오 : '))
print()
num_position(user)

while True:
    user_in = input('끝내시려면 1을 입력하세요.')
    if user_in == '1' :
        break