# 문제은행 1157 - 단어 속 최다 문자 출력 문제

# while True:
#     print("-" * 40)
#     user_in = input("최다 문자 출력 프로그램입니다.\n단어를 입력하세요.\n입력 -> ")
#     serch_list = []
#
#     jugNum = 0
#     serch_str = ""
#     serch_str_list = []
#     count_num_list = []
#
#     print("-" * 40)
#
#     if user_in == "":
#         print("프로그램을 종료합니다.")
#         break
#
#     for i in user_in:
#         serch_list.append(i.upper())
#
#     serch_list.sort()
#
#     for x in user_in:
#         if len(serch_list) == 0:
#             for i in count_num_list:
#                 if jugNum > i:
#                     continue
#                 elif jugNum == i:
#                     jugNum = -1
#                     break
#                 else:
#                     jugNum = i
#             if jugNum == -1:
#                 print("?")
#             else:
#                 print(serch_str_list[count_num_list.index(max(count_num_list))])
#             break
#         serch_str = serch_list[0]
#         serch_str_list.append(serch_str)
#         count_num_list.append(serch_list.count(serch_str))
#
#         for y in range(serch_list.count(serch_str)):
#             serch_list.remove(serch_str)

user_in = input().upper()
search_list = list(set(user_in))
count_list = []

for i in search_list:
    count_list.append(user_in.count(i))

if count_list.count(max(count_list)) >= 2:
    print("?")
else:
    print(search_list[(count_list.index(max(count_list)))])
