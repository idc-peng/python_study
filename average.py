A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
i = 0
average = 0

while i < 15:
    average = A[i] + average
    i += 1
    if i == 10:
        average = average / 10
        print("A 학급 평균은 %d 입니다." % average)
        break
