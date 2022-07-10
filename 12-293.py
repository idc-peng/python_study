dic = {}
with open('매수종목2.txt') as f:
    for i in f:
        (key, val) = .split()
        D[str(key)] = val

for key, val in D.items():
    print(key, val)
f.close()
