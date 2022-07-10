# while문을 사용한 1부터 5까지 계단식 출력하기

a = 0
b = 0
c = 5

while a < 5:
    while b < c:
        b += 1
        print(b, end = ' ')
    print()
    a += 1
    b = 0
    c -= 1