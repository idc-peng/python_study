# 문제 51 두 정수의 최대공약수

def max_div(num1, num2) :
    num1_list = []
    num2_list = []
    jdg = []
    
    for i in range(1, num1 + 1) :
        if num1 % i == 0 :
            num1_list.append(i)
         
    for x in range(1, num2 + 1) :
        if num2 % x == 0 :
            num2_list.append(x)
    
    for y in num1_list :
        for j in num2_list :
            if y == j :
                jdg.append(j)
                
      
    print()
    print('최대공약수 :', max(jdg))

user1 = int(input('첫 번째 정수를 입력하시오: '))
user2 = int(input('두 번째 정수를 입력하시오: '))
max_div(user1, user2)