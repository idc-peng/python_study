user = input("입력: ")

user_cash = user.split()

cash = int(user_cash[0])
unit = user_cash[1]

if unit == '달러' :
    rate = 1167
elif unit == '엔' :
    rate = 1.096
elif unit == '유로' :
    rate = 1268
elif unit == '위안' :
    rate = 171

print('%0.2f' % (rate * cash), '원')
