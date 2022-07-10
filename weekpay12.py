# 파이썬 과제 문제 12번 일별 근무시간 주급계산

Mon = int(input('월요일 근무시간을 입력하시오: '))
Tue = int(input('화요일 근무시간을 입력하시오: '))
Wed = int(input('수요일 근무시간을 입력하시오: '))
Thu = int(input('목요일 근무시간을 입력하시오: '))
Fri = int(input('금요일 근무시간을 입력하시오: '))

print()
pay = int(input("시간 당 급여를 입력하십시오: "))
total_pay = 0

if Mon >= 10 :
    total_pay = total_pay + (pay * 9) + ((Mon - 9) * pay * 1.3)
else :
    total_pay = total_pay + (Mon * pay)

if Tue >= 10 :
    total_pay = total_pay + (pay * 9) + ((Tue - 9) * pay * 1.3)
else :
    total_pay = total_pay + (Tue * pay)
    
if Wed >= 10 :
    total_pay = total_pay + (pay * 9) + ((Wed - 9) * pay * 1.3)
else :
    total_pay = total_pay + (Wed * pay)
    
if Thu >= 10 :
    total_pay = total_pay + (pay * 9) + ((Thu - 9) * pay * 1.3)
else :
    total_pay = total_pay + (Thu * pay)

if Fri >= 10 :
    total_pay = total_pay + (pay * 9) + ((Fri - 9) * pay * 1.3)
else :
    total_pay = total_pay + (Fri * pay)
    
print('-' * 25)
print("주급은 %d 입니다." % total_pay)