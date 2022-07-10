# 2020.04.14 문제 1

han = int(input("국어 성적을 입력하세요: "))
math = int(input("수학 성적을 입력하세요: "))
eng = int(input("영어 성적을 입력하세요: "))

print("입력받은 성적")
print('-' * 15)
print("국어 성적: %d" % han)
print("수학 성적: %d" % math)
print("영어 성적: %d" % eng)
print('-' * 15)

total = han + math + eng
avg = total / 3
print("총점은 %d 입니다." % total)
print("평균은 %0.2f 입니다." % avg)