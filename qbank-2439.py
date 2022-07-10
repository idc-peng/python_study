# 문제은행 2439번 - 별 찍기 (오른쪽 정렬)

user_in = int(input())

for x in range(1, user_in+1):
    for i in range(1, user_in+1):
        if (user_in - x) >= i:
            print(" ", end="")
        else:
            print("*", end="")
    print()
