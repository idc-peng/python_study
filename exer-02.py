# 약수 출력 받기

count = 0                                   # 약수의 개수

while True:                                 # user 에게서 정수를 입력 받는 과정
    user_num = input("양의 정수를 입력하시오: ")    
    
    try:
        int(user_num)
    except ValueError:                      # 실수 혹은 문자열을 입력 받았을 경우
        print("-" * 25)                     # 예외처리를 통해 다시 입력 받습니다.
        print("양의 정수가 아닙니다.")
        print("-" * 25)
        continue
        
    if int(user_num) <= 0:                  # 0 혹은 음의 정수를 받았을 경우
        print("-" * 25)
        print("양의 정수가 아닙니다.")
        print("-" * 25)
    else:
        num = int(user_num)                 # 양의 정수의 경우
        print()
        break
        
for i in range(1, num + 1):                 # 자기 자신도 포함해야되기 때문에 "num+1"을 range값에 넣습니다.
    jdg = num % i
    if jdg == 0:                            # 나눈 나머지가 0인 경우가 약수이므로 출력 및 count를 셉니다.
        print(i)
        count += 1                          

print()
print(num, "의 약수의 개수 : ", count)