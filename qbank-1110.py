user_in = int(input())
a = user_in // 10
b = user_in % 10
count = 1

while True:
    c = a + b
    result = b * 10 + ((a+b) % 10)

    if result == user_in:
        print(count)
        break
    else:
        a = result // 10
        b = result % 10
        count += 1

# 더하기 사이클
