# 문제은행 3058 - 짝수를 찾아라

while True:
    user_in = int(input("몇 번의 입력을 하시겠습니까?\n입력 -> "))
    result = 0
    b = []
    
    for i in range(user_in):
        a = input("7개의 숫자를 입력하시오.\n입력 -> ").split()
        
        for j in a:
            if int(j) % 2 == 0:
                result += int(j)
                b.append(int(j))
        print("%d %d" % (result, min(b)))
        
        a.clear()
        b.clear()
        result = 0