# 파이썬 13주차 과일재고관리 프로그램

import csv

while True:
    f = open("example.csv", 'r')
    a = csv.reader(f)
    user = input("과일이름을 입력하시오. ")
    if user == "" :
        break
    else :
        users = user[0].upper() + user[1:].lower()
        for i, j in a:
            if i == users:
                print(i, "의 재고수량은", j, "개 입니다.")
                f.close

print("-" * 20)    
print("프로그램을 종료합니다.")

f.close