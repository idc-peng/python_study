num_list = []
count = 1

for i in range(9):
    a = int(input())
    num_list.append(a)

for i in num_list:
    if i == max(num_list):
        print(max(num_list))
        print(count)
    else:
        count += 1

# 최댓값
