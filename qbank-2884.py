H, M = input().split()
h = int(H)
m = int(M)

m -= 45

if m < 0:
    m = 60 + m
    h -= 1
    if h < 0:
        h = 23

print("%d %d" % (h, m))

# 시간 계산기
