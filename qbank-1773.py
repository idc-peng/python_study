# 문제은행 1773 - 폭죽쇼

a, b = input("폭죽 학생 수, 끝나는 시간\n입력 -> ").split()
user_list = []
case_list = []

for i in range(int(a)):
    c = int(input("시간 -> "))
    user_list.append(c)

for f in user_list:
    num = int(b) // f
    for x in range(1, num + 1):
        case_list.append(x*f)

for j in case_list:
    if  case_list.count(j) != 1:
        case_list.remove(j)

print(len(case_list))