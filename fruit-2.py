import csv

def lookup():
    o = dic.keys()
    i = dic.values()
    print(o)
    print(i)
    
def add(user):
    if user in dic:
        for i, j in dic.items():
            if i == user:
                menu_add = int(input("추가할 수량을 입력하시오."))
                num1 = int(j) + menu_add
                dic[i] = num1
                print(i, "의 바뀐 수량은", num1, "입니다.")
                break
    else:
        menu = input("새로운 과일을 생성하겠습니까?(추가:1)(취소:2)")
        if menu == "1":
            menu_num = int(input("수량을 입력하시오."))
            print("추가됬습니다.")
            dic[user] = menu_num
        elif menu == "2":
            print("취소됬습니다.")
            
def minus(user):
    for i, j in dic.items():
        if i == user:
            print(i, "의 수량은", j, "입니다.")
            menu_minus = int(input("뺄 수량을 입력하시오."))
            num2 = int(j) - menu_minus
            dic[i] = num2
            print(i, "의 바뀐 수량은", num2, "입니다.")
            
def delete(user):
    for i in dic.keys():
        if i == user:
            menu_user = input("정말로 삭제를 하시겠습니까?(삭제:1)(취소:2)")
            if menu_user == "1":
                del dic[i]
                break
            elif menu_user == "2":
                print("취소됬습니다.")
                break

f = open("example.csv", 'r')
a = csv.reader(f)
dic = {}

for x, y in a:
	dic[x] = y

while True:
    user_in = input("조회(q), 추가(a), 빼기(m), 과일삭제(d) 중 고르시오. ")
    if user_in == "" :
        count = 0
        f = open("example.csv", 'w', newline='')
        wr = csv.writer(f)
        wr.writerow(dic.keys())
        wr.writerow(dic.values())       
        print("-" * 60)
        print("종료되었습니다.")
        break
        
    if user_in == "q" :
        d = lookup()
        continue
    user_fruit = input("원하는 과일을 입력하시오.")
    users = user_fruit[0].upper() + user_fruit[1:].lower()
    if user_in == "a" :
        d = add(users)
    elif user_in == "m" :
        d = minus(users)
    elif user_in == "d" :
        d = delete(users)
        
    print("-" * 60)
    
f.close()