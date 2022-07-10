# 문제은행 10984 - 학점 구하기

while True:
    user_in = int(input("학기 수를 입력하시오.\n입력란 -> "))
    score = 0
    sums = 0
    sco_lis = []
    sums_lis = []    
    
    for i in range(user_in):
        b = int(input("수업 수를 입력하시오.\n입력란 -> "))
        
        for x in range(b):
            c, d = input("학점과 점수를 입력하시오.\n입력란 -> ").split()
            
            sums += (int(c) * float(d))
            score += int(c)
        sco_lis.append(score)
        sums_lis.append(sums/score)
        sums = 0
        score = 0
        count = 0
    
    for i in range(user_in):
        print("%d %0.1f" % (sco_lis[i], sums_lis[i]))