#주급 계산 program 문제 11번

work_time = int(input("근무 시간을 입력하십시오: "))
pay = int(input("시간 당 급여를 입력하십시오: "))
print()

if work_time > 45 :
    if (work_time - 45) < 13 :
        real_pay = (pay * 45) + ((work_time - 45) * pay * 1.3)
    else :
        real_pay = (pay * 45) + (pay * 12 * 1.3) + ((work_time - 57) * pay * 1.5)
else:
    real_pay = work_time * pay
    
print('-' * 25)
print("주급은 %d 입니다." % real_pay)