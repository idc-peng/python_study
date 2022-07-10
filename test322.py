# 문제27번 성적 계산 프로그램

f = open('C:/Users/cgj10/python/score-01.txt', 'r')

total = 0
count = 0
f_list = []
array_list = []

for i in f:
    f_list.append(i.split())

for i in f_list:
    print("입력 성적:", i)
    for j in i:
        total += int(j)
        count += 1
    for x in range(count):
        array_list.append(max(i))
        i.remove(max(i))
    print("성적 순서:", array_list)    
    print("평균 성적: %0.2f" % (total/count))
    total = 0
    count = 0
    array_list.clear()
    print("-" * 20)

f.close()
