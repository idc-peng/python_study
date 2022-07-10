print("입력값: ", end=' ')
user = input()
number = int(user) - 20

if 0 <= number <= 255 :
    print("출력값: %d" % number)
elif number < 0 :
    print("출력값: 0")
else :
    print("출력값: 255")
