user = input("주민등록번호('-' 포함): ")

jug = user[7]

if jug == '1' or jug == '3':
    print("남자")
elif jug == '2' or jug == '4':
    print('여자')
else:
    print("올바르지 않은 주민등록번호입니다.")
