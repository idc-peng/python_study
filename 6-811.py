# for문 사용하여 한 글자씩 듸어서 만들기 (2회 출력)

a = 0

for i in range(1, 12):
    a += 1
    if a == 6 :
        a = 0
        continue
    else :
        print(a, end = ' ')