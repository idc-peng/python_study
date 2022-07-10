# while문을 이용한 1부터 5까지 계단식 출력 변형

a = 1
b = 1
c = 1

while a < 6:
    while c < a:
        c += 1
        print(' ', end = ' ')
    while b < 6:
        print(b, end = ' ')
        b += 1
    print()
    a += 1
    b = a
    c = 1