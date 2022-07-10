# 문제은행 10950 - 더하기 프로그램

user_in = int(input())
cal_list = []

for i in range(user_in):
    a, b = input().split()
    cal_list.append((int(a) + int(b)))

for i in cal_list:
    print(i)
