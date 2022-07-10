# list 자료구조를 이용한 데이터 분석

data_a = []
b = 0
even = 0
add = 0
mult_3 = 0

while True:
    b = int(input("값을 입력해주세요: "))
    if b >= 0:
        data_a.append(b)
    else:
        break

for i in data_a:
    if i < 0 :
        break
    if i % 2 == 0:
        even += 1
    else:
        add += 1
    if i % 3 == 0:
        mult_3 += 1

if len(data_a) == 0:
    print("처음부터 음수값을 받아 프로그램을 종료합니다.")
    
print("짝수의 개수: ", even)
print("홀수의 개수: ", add)
print("3의 배수: ", mult_3)