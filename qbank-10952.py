num_list = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    num_list.append(a + b)

for i in num_list:
    print(i)

# A+B - 5
