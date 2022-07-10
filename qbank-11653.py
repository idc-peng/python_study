# 문제은행 11653 - 소인수분해

def prime_number(num):
    prime_num = num
    for i in range(2, num+1):
        for x in range(2, (i+1)):
            if (i % x) == 0:
                while True:
                    if prime_num % x == 0:
                        print(x)
                        prime_num = prime_num / x
                    else:
                        break
            else:
                continue
    
    if prime_num == 1:
        pass
    else:
        print(prime_num)

while True:
    user_in = int(input("소인수분해를 할 숫자를 입력하세요.\n입력란 -> "))
    
    prime_number(user_in)