# for문 1부터 5까지 출력 (점점 감소하는 형식)

a = 6

for i in range(1, 6):
    for s in range(1, a):
        print(s, end = ' ')
        
    print()
    a -= 1