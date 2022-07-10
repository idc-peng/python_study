def num_count(num):
    result = 0
    for q in range(1, num+1):
        result += q
    return result


loop = int(input())     # 루프 횟수
ox_list = []            # ox리스트
sum_num = 0             # 합계
count = 0               # 카운트
num_list = []           # 점수

for i in range(loop):
    a = input()
    ox_list = list(a)

    for x in ox_list:
        if x == "O":
            count += 1
        else:
            b = num_count(count)
            sum_num += b
            count = 0
    if count != 0:
        b = num_count(count)
        sum_num += b

    num_list.append(sum_num)

    sum_num = 0
    count = 0
    ox_list.clear()

for i in num_list:
    print(i)

# OX퀴즈
