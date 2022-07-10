# 문제은행 9506 - 완전수

def jug(lis):
    for i in lis:
        b = []
        b = divisor(i)
        num = 0
        
        for a in b:
            num += a
        if num == i:
            print("%d =" % num, end = " ")
            for x in b:
                if x == b[len(b)-1]:
                    print("%d" % x)
                else:
                    print("%d +" % x, end = " ")
        else:
            print("%d is NOT perfect." % i)
    print()
        
def divisor(num):
    nu_lis = []
    
    for i in range(1, num):
        if num % i == 0:
            nu_lis.append(i)
            
    return nu_lis

while True:
    num_lis = []
    
    while True:
        user_in = int(input("수를 입력하세요~\n"))
        if user_in == -1 :
            break
        num_lis.append(user_in)
    jug(num_lis)