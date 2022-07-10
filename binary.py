# binary (진수변환 프로그램)

def octal(lst):                         # 2진수 -> 8진수 변환 함수
    count = 0                           # 2진수를 8진수로 변환하기 위해 3 자리씩 계산하였습니다.
    binary = 1                          # 2의 0승 부터 2의 2승까지를 계산하기 위한 수
    sums = 0                            # 8진수의 자리수를 나타내기 위한 수
    total_list = []
    jug = 0                             # 리스트의 길이가 3의 배수가 아닌 경우를 판별하는 수
    result = 0                          # return 값
    octa = ""                           # 8진수 변환 최종 값
    
    for i in lst:
        sums = sums + (i * binary)
        count += 1
        jug += 1

        if count == 3 or len(lst) == jug and len(lst) % 3 != 0 :
            total_list.append(str(sums))
            sums = 0
            binary = 1
            count = 0
        else :
            binary =  binary * 2
    total_list.reverse()
    for i in total_list :
        octa = octa + str(i)
        
    return octa
    

def decimal(lst) :                      # 2진수 -> 10진수 변환 함수
    binary = 1                          # 2의 계승을 나타내기 위한 수
    result = 0                          # 10진수 값을 합산하고 return하기 위한 수
    
    for i in lst:
        result = result + (i * binary)
        binary = binary * 2
        
    return result

def hexa(lst) :                         # 2진수 -> 16진수 변환 함수
    count = 0                           # 2진수를 16진수로 변환하기 위해 4 자리씩 계산하였습니다.
    binary = 1                          # 2의 0승 부터 2의 3승까지를 계산하기 위한 수
    sums = 0
    total_list = []
    jug = 0                             # 리스트의 길이가 4의 배수가 아닌 경우를 판별하는 수
    result = 0                          # return 값
    hexas = ""                          # 16진수 변환 최종 값
    liter = ""
    
    for i in lst:
        sums = sums + (i * binary)
        count += 1
        jug += 1
        if count == 4 or len(lst) == jug and len(lst) % 4 != 0 :
            if sums == 10:
                liter = "A"
            elif sums == 11:
                liter = "B"
            elif sums == 12:
                liter = "C"
            elif sums == 13:
                liter = "D"
            elif sums == 14:
                liter = "E"
            elif sums == 15:
                liter = "F"
            else :
                liter = str(sums)
            total_list.append(str(liter))
            sums = 0
            binary = 1
            count = 0
        else :
            binary =  binary * 2
    total_list.reverse()
    for i in total_list :
        hexas = hexas + str(i)
        
    return hexas

while True:                             # 무한 루프로 반복 횟수 무한
    try:
        user_in = input("슷자를 입력하시오.")
        user_list = []
        jug = 0                         # 만약 2진수가 아닌 경우 1을 더해서 판단하는 변수
        
        if user_in == "":               # 엔터 시 종료
            print("-" * 25)
            print("\n프로그램을 종료합니다.")
            break
    
        for i in user_in:
            if i == "1" or i == "0" :   # 0과 1 즉 i가 2진수인지 판별
                user_list.append(int(i))
            else :                      # 2진수가 아닐 시 jug += 1 을 하여 다시 반복하도록 구성하였습니다.
                print("-" * 25)
                print("2진수가 아닙니다.")
                print("-" * 25)
                jug += 1
                break
                
        if jug == 1:
            continue
        elif len(user_list) > 9 :       # 입력 값의 최대 길이를 넘었을 시
            print("-" * 25)
            print("범위 초과입니다.\n다시 입력하세요.")
            print("-" * 25)
            continue
        
        for i in user_list :
            if user_list[0] == 0 :
                user_list.remove(0)
            else :
                break
        user_list.reverse()             # 진수 계산을 용이하게 하기 위해서 list를 reverse하였습니다.
        
        print("-" * 25)
        print("(메뉴)")
        print("\t1 : 2진수 --> 8진수 변환")
        print("\t2 : 2진수 --> 10진수 변환")
        print("\t3 : 2진수 --> 16진수 변환")
        print("-" * 25)
        user_num = input("원하시는 메뉴 입력 : ")
        
        if user_num == "1" :
            octa_num = octal(user_list)
            print("진수변환:", user_in, "(2진수)", "--->", "변환값", octa_num, "(8진수)")
        elif user_num == "2" :c
            deci_num = decimal(user_list)
            print("진수변환:", user_in, "(2진수)", "--->", "변환값", deci_num, "(10진수)")
        elif user_num == "3" :
            hexa_num = hexa(user_list)
            print("진수변환:", user_in, "(2진수)", "--->", "변환값", hexa_num, "(16진수)")
        else :
            print("메뉴에 해당되지 않습니다.\n다시 입력해주세요.")
        
    except ValueError:                  # 마이너스나 문자가 입력되었을 시 다시 시작하도록 구성하였습니다.
        print("숫자가 아닌 문자가 들어있습니다.")
        