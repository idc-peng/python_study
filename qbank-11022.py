loop = int(input())
a_list = []
b_list = []

for i in range(loop):
    a, b = map(int,input().split())
    a_list.append(a)
    b_list.append(b)

for i in range(loop):
    print("Case #%d: %d + %d = %d" % (i+1, a_list[i], b_list[i], a_list[i]+b_list[i]))

# A+B - 8
