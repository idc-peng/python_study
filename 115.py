user_num = input('휴대전화 번호 입력("-" 포함): ')

phone = user_num.split('-')
jug = phone[0]


if jug == '011':
    print("당신은 SKT 사용자입니다.")
elif jug == '016' :
    print("당신은 KT 사용자입니다.")
elif jug == '019' :
    print("당신은 LGU 사용자입니다.")
else :
    print("알수없습니다.")

