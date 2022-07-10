loop = int(input())
num_list = []

for i in range(loop):
    a, b = map(int,input().split())
    num_list.append(a+b)

for i in range(loop):
    print("Case #%d: %d" % (i+1, num_list[i]))

# A+B - 7
