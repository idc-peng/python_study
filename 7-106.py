# list 자료구조를 이용한 for문 1부터 5까지 계단식 출력

a = [0, 1, 2, 3, 4]
b = [4, 3, 2, 1, 0]

for i in a:
    for j in b:
        print(len(a)-j, end = ' ')
    print()
    b.remove(i)