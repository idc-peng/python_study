# 문제28번 성적 계산 프로그램 (심화)

a = 0
b = 0
total = 0
score = []
fir_score = []

for i in range(5):
    while True:
        a = int(input("성적을 입력하시오 : "))
        if 0 <= a <= 100:
            score.append(a)
            break
        else:
            print('0부터 100까지의 수를 입력하시오.')
            continue

fir_score = score
print()
print('성적 순서:', fir_score)

for o in range(5):
    for j in [1,2,3,4]:
        if score[j] > score[j-1]:
            b = score[j]
            score[j] = score[j-1]
            score[j-1] = b
        else:
            continue
    total += score[o]

print('성적 순서:', score)
print('평균 성적: %0.2f' % (total / 5))