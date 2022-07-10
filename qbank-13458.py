# 문제은행 13458 - 시험감독

while True:
    user_exam = int(input("시험장의 개수 : "))
    user_peo = input("응시자의 수 : ").split()
    mag_all, mag = input("감시 능력 : ").split()
    people = 0
    count_num = 0
    count = []
    
    if user_exam != len(user_peo):
        pritn("응시생의 수가 다릅니다.")
        continue
    
    for i in user_peo:
        people = int(i) - int(mag_all)
        count_num += 1
        
        if people > 0:
            while True:
                if people > 0:
                    people -= int(mag)
                    count_num += 1
                else:
                    break
        count.append(count_num)
        count_num = 0
    
    print("필요한 감독관의 수는 %d 입니다." % sum(count))