import sys


for_num = int(sys.stdin.readline())
num_list = []

for i in range(for_num):
    A, B = map(int, sys.stdin.readline().split())
    num_list.append(A+B)

for i in range(for_num):
    print(num_list[i])

# 처음 보는 방법 map(int, sys.stdin.readline().split()) == int(input()).split()
