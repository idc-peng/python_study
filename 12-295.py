dic = {}
with open('매수종목2.txt') as f:
    for i in f:
        (key, val) = i.split()
        dic[str(key)] = val

for key, val in dic.items():
    print(key, val)

print(dic)
f.close()
