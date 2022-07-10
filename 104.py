print("0이상의 정수를 입력하시오.")
user = input()
num_20 = int(user) + 20

if 0 <= num_20 <= 255 :
    print("출력값: %d" % num_20)
elif num_20 > 255:
    print("출력값: 255")
else:
    print("출력값: 0")
