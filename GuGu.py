def GuGuDan(num1, num2):
    for i in range(1, num2 + 1):
        print(num1, "*", i, "=", num1 * i)

while(True):
    user_num1 = int(input("구구단 몇 단을 보고 싶으신가요?"))
    user_num2 = int(input("몇까지 곱을 보고 싶나요?"))

    GuGuDan(user_num1, user_num2)

    print("-" * 25)
    user_in = input("그만할까요?\n원하시면 엔터 더 하시고 싶으시면 다른키")

    if user_in == "" :
        break
    else:
        continue
