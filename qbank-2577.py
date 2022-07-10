A = int(input())
B = int(input())
C = int(input())

num_list = list(str(A * B * C))

for i in range(10):
    print(num_list.count(str(i)))

# 숫자의 개수
