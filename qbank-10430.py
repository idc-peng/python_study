# 세 숫자로 나머지 경우별 비교

A, B, C = input().split()
a = int(A)
b = int(B)
c = int(C)
print("%d" % ((a+b)%c))
print("%d" % (((a%c) + (b%c))%c))
print("%d" % ((a*b)%c))
print("%d" % (((a%c) * (b%c))%c))
