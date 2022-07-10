# list 자료구조를 이용한 for문 1부터 5까지 계단식 출력

a = [4, 3, 2, 1, 0]
b = [4, 3, 2, 1, 0]
c = []

for i in a:
    for j in c:
        print(' ', end = ' ')
    for o in b:
        print(len(a) - o, end = ' ')
    print()
    b.remove(i)
    c.append(0)