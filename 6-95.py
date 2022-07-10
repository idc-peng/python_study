# while문을 사용하여 1부터 5까지 가로출력 5회

a = 0
b = 0

while a < 5:
    while b < 5:
        b += 1
        print(b, end = ' ')
    print()
    a += 1
    b = 0