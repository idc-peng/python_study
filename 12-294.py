i = open("C:/Users/cgj10/python/매수종목1.txt", 'r')
line = i.readlines()
print(line)
i.close()

f = open("C:/Users/cgj10/python/매수종목1.txt", 'a')

data = "005930\n"
data1 = "005380\n"
data2 = "035420\n"
f.write(data)
f.write(data1)
f.write(data2)
f.close()
