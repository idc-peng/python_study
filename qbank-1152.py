# 문제은행 1152 - 단어 개수 확인

# while True:
#     user_in = input("문장 속 단어 개수 프로그램입니다.\n입력 -> ")
#     lis = []
#
#     if user_in == "":
#         print("프로그램을 종료합니다.")
#         break
#
#     lis.extend(user_in.split())
#     print(len(lis))

user_in = input()
lis = []

lis.extend(user_in.split())
print(len(lis))
