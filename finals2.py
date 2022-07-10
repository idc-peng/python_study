data1 = [["apple", "banana", "cherry", "berry", "grape" ],[ 10, 30, 50, 20, 40 ]]
result = []

jug = []
data_lis1 = data1[0]
data_lis2 = data1[1]

for i in range(len(data_lis1)):
    num_index = data_lis2[i]
    data_str = data_lis1[i]
    for j in range(len(data_lis1)):
        if num_index > data_lis2[j]:
            data_lis2[i] = data_lis2[j]
            data_lis2[j] = num_index
            data_lis1[i] = data_lis1[j]
            data_lis1[j] = data_str
            num_index = data_lis2[i]
            data_str = data_lis1[i]
        if num_index == data_lis2[j]:
            if ord(data_str[0]) > ord(data_lis1[j][0]):
                pass
            else:
                data_lis2[i] = data_lis2[j]
                data_lis2[j] = num_index
                data_lis1[i] = data_lis1[j]
                data_lis1[j] = data_str
                num_index = data_lis2[i]
                data_str = data_lis1[i]
                
result.append(data_lis1)
result.append(data_lis2)

print("과일재고 수량 (내림차순)")

for i in range(2):
    for x in range(5):
        print(result[i][x], end = " ")
    print()