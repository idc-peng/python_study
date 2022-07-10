# 문제26번 성적 계산 프로그램

a = 0
score = []

for i in range(5):
    while True:
        a = int(input("성적을 입력하시오 : "))
        if 0 <= a <= 100:
            score.append(a)
            break
        else:
            print('0부터 100까지의 수를 입력하시오.')
            continue

print()
print('입력한 성적들', score)
print('최고 성적 :', max(score))
print('최저 성적 :', min(score))
print('평균 : %0.2f' % (sum(score) / len(score)))