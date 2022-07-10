# 문제은행 2502 - 떡 먹는 호랭이

a, b = input("정보를 입력하시오\n입력 -> ").split()
num_list = []

for x in range(1, int(b)):
    for i in range(1, int(b)):
        num_list.append(x)
        num_list.append(i)
        for j in range(int(a) - 2):
            num = num_list[j] + num_list[j+1]
            num_list.append(num)
        if num_list[int(a) - 1] == int(b):
            break
        num_list.clear()
    
print("%d, %d" % (num_list[0], num_list[1]))