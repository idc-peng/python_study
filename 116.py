user = input("우편번호: ")

zip = int(user[2])

if zip == 0 or zip == 1 or zip == 2:
    print('강북구')
elif zip == 3 or zip == 4 or zip == 5:
    print('도봉구')
else:
    print('노원구')
