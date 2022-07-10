# 문제은행 11399 - atm 문제
# ※※※ 새로운 내용 input으로 리스트도 만들 수 있다. split() 매서드 사용

while True:
    user_in = int(input("줄 서있는 사람 수를 입력하세요.\n숫자만!!!\n입력 -> "))
    count = 0
    result = 0
    people_list = []
    
    user_list = input("몇 분의 시간이 걸리나요?\n-> ").split()
        
    for i in user_list:
        people_list.append(int(i))
                
    people_list.sort()
    
    if len(people_list) == user_in:
        for i in range(user_in):
            count += people_list[0]
            people_list.remove(min(people_list))
            result += count
    else:
        print("----- 사람 수와 시간 수가 다릅니다. -----")
    print(result)