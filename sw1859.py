# sw 1859 백만 장자 프로젝트 (사재기)

def fun0(num, lis):
    result = []
    pos = 0
    count = 0

    for x in range(len(lis)-1):
        pos += 1
        if count >= 1:
            count -= 1
            continue
        if lis[x] > lis[pos]:
            result.append(lis[x] - lis[pos])
            if pos != (num-1):
                if lis[x] > lis[pos+1]:
                    result.append(lis[x] - lis[pos+1])
                    count += 2

    # for x in range((num//3)):
    #     for y in lis[x:x+2]:
    #         if int(y) < int(lis[x+2]):
    #             result.append(int(lis[x+2]) - int(y))

    return result


# def fun1(num1, num2, lis):
#     result = []
#
#     for x in range((user_in//3 + 1)):
#         if (num2 + 1) == x:
#             print(1)
#     return 1
#
#
# def fun2(num1, num2, lis):
#     return 1

user_day = int(input("몇 일 동안 매매를 합니까? -> "))
benefit_list = []

for i in range(user_day):
    user_in = int(input("테스트케이스 -> "))
    user_list = (input("매매가 -> ")).split()
    # quo = user_in // 3

    user_list_change = list(map(int, user_list))

    if user_in != len(user_list_change):
        print("테스트 케이스와 매매가의 개수가 다릅니다.")
        break
    for l in user_list_change:
        if l > 10000 or l < 0 :
            print("범위값 오류")
            break

    user_list_change.reverse()

    # if user_in % 3 == 0:
    benefit_list = fun0(user_in, user_list_change)
    # elif user_in % 3 == 1:
    #     benefit_list = fun1(user_in, quo, user_list_change)
    # else:
    #     benefit_list = fun2(user_in, quo, user_list_change)

    print("#%d %d" % (i+1, sum(benefit_list)))

    benefit_list.clear()