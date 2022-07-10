# 문제 16 일별 근무시간 입력

def work_pay (day_list, pays) :
    total = 0
    for i in day_list[:5] :
        if i > 9 :
            total = total + (i * pays) + ((i-9) * pays * 1.3)
        else :
            total = total + (i * pays)
    
    for x in day_list[5:] :
        if i > 9 :
            total = total + (i * pays) + ((i-9) * pays * 2.0)
        else :
            total = total + (x * pays)
            
    return total
    
user_list = []
user = 0
pay = 0

while True :
    for i in range(5) :
        user = int(input('월요일부터 일요일까지 근무시간을 한 번씩 입력하시오: '))
        if user > 13 :
            print('잘못 입력되었으므로 다시 입력해주십시오.')
            i -= 1
            continue
        user_list.append(user)
        
        if len(user_list) == 7 :
            break
    if len(user_list) == 7 :
        break
        
pay = int(input('시급을 입력하시오: '))

week_pay = work_pay(user_list, pay)
print('-' * 20)
print(week_pay)