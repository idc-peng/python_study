# 문제27번 성적 계산 프로그램

f = open('C:/Users/cgj10/python/score-01.txt', 'r')

total = 0               # 점수 계산
count = 0               # len을 대신하여 리스트의 요소의 개수를 계산
f_list = []             # score-01의 리스트
array_list = []         # 성적 순서 리스트

for i in f:             # f_list에 리스트 형태로 txt를 저장
    f_list.append(i.split())

for i in f_list:        # 리스트의 줄만큰(각 학생의 성적만큼) 반복
    print("입력 성적:", i)
    for j in i:         # 학생의 평균 계산 및 성적의 개수 조사
        total += int(j)
        count += 1
    for x in range(count):  # 학생의 성적 순서 리스트
        array_list.append(max(i))
        i.remove(max(i))
    print("성적 순서:", array_list)
    print("평균 성적: %0.2f" % (total/count))
    total = 0           # 한 학생이 계산할 때 마다 초기화
    count = 0
    array_list.clear()
    print("-" * 20)

f.close()