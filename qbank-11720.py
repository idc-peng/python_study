user_in = int(input())
user_list = input()

a = list(map(int, user_list))
if len(a) == user_in:
    print(sum(a))

# 숫자의 합
