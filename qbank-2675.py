loop = int(input())
lis_a = []
lis_b = []
count = 0

for i in range(loop):
    a, b = input().split()
    lis_a.append(int(a))
    lis_b.append(b)

for j in lis_a:
    for y in lis_b[count]:
        for x in range(j):
            print(y, end="")
    count += 1
    print()

# 문자열 반복
