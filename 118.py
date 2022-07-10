user = input("주민등록번호('-'포함): ")

jug = int(user[8:10])

if jug <= 8:
    print("서울 입니다.")
elif jug <= 12:
    print("부산 입니다.")
else:
    print("서울이 아닙니다.")
