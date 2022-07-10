one = int(input('input number1: '))
two = int(input('input number2: '))
thr = int(input('input number3: '))

jug = 0

if one > two :
    jug = one
else:
    jug = two

if thr > jug :
    jug = thr

print(jug)
