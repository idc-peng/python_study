# while문을 사용한 1부터 5까지 가로 출력 2회

a = 0
b = 0

while a < 2 :
    while b < 5 :
        b += 1
        print(b, end = ' ')
    print()
    a +=1
    b = 0