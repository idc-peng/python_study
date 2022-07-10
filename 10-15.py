# 문제 15 일별 근무시간 입력

def work_pay (day_list, pays) :
    total = 0
    for i in day_list :
        if i > 9 :
            total = total + (i * pays) + ((i-9) * pays * 1.3)
        else :
            total = total + (i * pays)
            
    return total
    
user_list = []
user = 0
pay = 0
        
for i in range(5) :
    user = int(input('월요일부터 금요일까지 근무시간을 한 번씩 입력하시오: '))
    user_list.append(user)
pay = int(input('시급을 입력하시오: '))

week_pay = work_pay(user_list, pay)
print('-' * 20)
print(week_pay)