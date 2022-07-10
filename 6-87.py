# for문 1부터 5까지 출력 (점점 앞에 문자가 없어지는 형식)

a = 1

for i in range(2, 7):
    for s in range(i-2):
        print(' ', end = ' ')
    for o in range(i-1, 6):
        print(o, end = ' ')
    print()