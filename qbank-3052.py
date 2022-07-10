num_list = []
jdg = 0

for i in range(10):
    a = int(input())

    for x in num_list:
        if x == (a % 42):
            jdg += 1
            break

    if jdg == 1:
        pass
    else:
        num_list.append((a % 42))
    jdg = 0

print(len(num_list))

# 나머지
