# 문제은행 2588 - 세 자리 수 곱셈과정

def fir(x, num1):
    a = int(num1)
    
    return x * a


def sec(x, num2):
    b = int(num2)
    
    return x * b


def thi(x, num3):
    c = int(num3)
    
    return x * c


first_num = int(input())
sec_num = input()
num_list = []

for i in sec_num:
    num_list.append(i)

fir_num = fir(first_num, num_list[2])

sec_num = sec(first_num, num_list[1])

thi_num = thi(first_num, num_list[0])

print(fir_num)
print(sec_num)
print(thi_num)
print("%d" % (fir_num + (sec_num * 10) + (thi_num * 100)))
