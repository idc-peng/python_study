# 문제은행 10178 - 할로윈의 사탕

def caca(num):
    for i in range(num):
        a, b = input("case %d -> " % (i+1)).split()
        print("You get %d piece(s) and your dad gets %d piece(s)." % ((int(a) // int(b)), (int(a) % (int(b)))))
    
while True:a
    user_in = int(input("몇 번의 케이스?\n입력 -> "))

    caca(user_in)