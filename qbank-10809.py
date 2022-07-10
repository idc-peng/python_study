user_in = list(map(str, input()))
abc = "abcdefghijklmnopqrstuvwxyz"

for i in abc:
    if i in user_in:
        print(user_in.index(i), end=' ')
    else:
        print( -1, end=' ')


# 알파벳 찾기
