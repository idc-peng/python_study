f = open("C:/Users/cgj10/python/새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
