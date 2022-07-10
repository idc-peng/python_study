jdg, main_num = map(int, input().split())
number = input().split()
min_list = []

for i in number:
    if main_num > int(i):
        min_list.append(int(i))

for x in min_list:
    print(x, end=" ")

# X보다 작은 수
