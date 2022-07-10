# 약수 구하기

import csv

f = open('in_data.csv', 'r')
a = csv.reader(f)
b = []

for i in a:
    for x in range(8):
        print(type(i[x]))
        c = int(i[x])
        print(c)
        print(type(c))

f.close()