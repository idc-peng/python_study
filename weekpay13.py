# 파이썬 과제 문제 12번 일별 근무시간 주급계산

week_time = []

week_time.append(input('월요일 근무시간을 입력하시오: '))
week_time.append(input('화요일 근무시간을 입력하시오: '))
week_time.append(input('수요일 근무시간을 입력하시오: '))
week_time.append(input('목요일 근무시간을 입력하시오: '))
week_time.append(input('금요일 근무시간을 입력하시오: '))
week_time.append(input('토요일 근무시간을 입력하시오: '))
week_time.append(input('일요일 근무시간을 입력하시오: '))

pay = int(input("시간 당 급여를 입력하십시오: "))
total_pay = 0

if int(week_time[0]) >= 10 :
    total_pay = total_pay + (pay * 9) + ((int(week_time[0]) - 9) * pay * 1.3)
else :
    total_pay = total_pay + (int(week_time[0]) * pay)
    
if int(week_time[1]) >= 10 :
    total_pay = total_pay + (pay * 9) + ((int(week_time[1]) - 9) * pay * 1.3)
else :
    total_pay = total_pay + (int(week_time[1]) * pay)

if int(week_time[2]) >= 10 :
    total_pay = total_pay + (pay * 9) + ((int(week_time[2]) - 9) * pay * 1.3)
else :
    total_pay = total_pay + (int(week_time[2]) * pay)

if int(week_time[3]) >= 10 :
    total_pay = total_pay + (pay * 9) + ((int(week_time[3]) - 9) * pay * 1.3)
else :
    total_pay = total_pay + (int(week_time[3]) * pay)

if int(week_time[4]) >= 10 :
    total_pay = total_pay + (pay * 9) + ((int(week_time[4]) - 9) * pay * 1.3)
else :
    total_pay = total_pay + (int(week_time[4]) * pay)

if int(week_time[5]) >= 10 :
    total_pay = total_pay + (pay * 9) + ((int(week_time[5]) - 9) * pay * 2.0)
else :
    total_pay = total_pay + (int(week_time[5]) * pay)

if int(week_time[6]) >= 10 :
    total_pay = total_pay + (pay * 9) + ((int(week_time[6]) - 9) * pay * 2.0)
else :
    total_pay = total_pay + (int(week_time[6]) * pay)
    
print('-' * 25)
print("주급은 %d 입니다." % total_pay)