# 문제은행 2720 - 세탁소 사장 동혁

user_in = int(input("테스트 케이스 횟수 -> "))
num_list = []
money = 0

for i in range(user_in):
    a = int(input("돈을 입력하세요\n입력 -> "))
    num_list.append(a)

for i in num_list:
    money = i
    
    q = money // 25
    money -= q*25
    
    d = money // 10
    money -= d*10
    
    n = money // 5
    money -= n*5
    
    p = money // 1
    
    print("%d %d %d %d" % (q, d, n, p))