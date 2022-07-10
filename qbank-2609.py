# 문제은행 2609 - 최대공약수, 최소공배수

while True:
    num1, num2 = input("두 수를 입력하시오.\n->").split()
    num_min_list = []
    num_minofmax = 0
    num_maxofmin = 0 

    if int(num1) == int(num2):
        print("최대공약수는 %s , 최소공배수는 %s 입니다." % (num1, num1))
    elif int(num1) > int(num2):
        for i in range(1, int(num1) + 1):
            if int(num1) % i == 0 and int(num2) % i == 0:
                num_min_list.append(i)
        num_minofmax = max(num_min_list)
        num_maxofmin = (int(num1)/num_minofmax) * (int(num2)/num_minofmax) * num_minofmax
        print("최대공약수는 %d , 최소공배수는 %d 입니다." % (num_minofmax, num_maxofmin))
    else:
        for i in range(1, int(num2) + 1):
            if int(num1) % i == 0 and int(num2) % i == 0:
                num_min_list.append(i)
        num_minofmax = max(num_min_list)
        num_maxofmin = (int(num1)/num_minofmax) * (int(num2)/num_minofmax) * num_minofmax
        print("최대공약수는 %d , 최소공배수는 %d 입니다." % (num_minofmax, num_maxofmin))
    