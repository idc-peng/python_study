loop = int(input())

num_list = list(map(int, input().split()))
num_list_sum = 0

if len(num_list) == loop:
    for i in num_list:
        num_list_sum += (i/max(num_list) * 100)

    print((num_list_sum / len(num_list)))

# 평균
