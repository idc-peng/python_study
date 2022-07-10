print("현재시간", end=' ')
user = input()
minute = user[3:]

if minute == "00" :
    print("정각입니다.")
else :
    print("정각이 아닙니다.")
