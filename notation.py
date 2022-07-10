# 중간시험 대체과제
# 모든 함수에 return 값을 사용하였고 함수 내부에서 출력하고 return값 없이 구성도 가능하나, 각각 return 값을 주고 각각 return 받은 값을 출력하도록 구성하였습니다.

def binary_8(lst):                                                  # 2진수 8진수 변환
    count = 0
    binary = 1
    sums = 0
    total_list = []
    jug = 0
    result = 0
    octa = ""
    
    for i in lst:
        sums = sums + (int(i) * binary)
        count += 1
        jug += 1

        if count == 3 or len(lst) == jug and len(lst) % 3 != 0 :    # 3자리가 묶였거나, 자리수를 다 계산하였지만 3자리가 안 묶였을 경우에는 8진수로 변환하여 반환하였습니다.
            total_list.append(str(sums))
            sums = 0
            binary = 1
            count = 0
        else :
            binary =  binary * 2
    total_list.reverse()
    for i in total_list :                                           # 모든 함수는 str로 반환하였습니다.
        octa = octa + str(i)
    
    return octa
    
def binary_10(lst):                                                 # 2진수 10진수 변환
    binary = 1
    result = 0
    
    for i in lst:
        result = result + (i * binary)
        binary = binary * 2
        
    return result

def binary_16(lst):                                                 # 2진수 16진수 변환
    count = 0
    binary = 1
    sums = 0
    total_list = []
    jug = 0
    result = 0
    hexas = ""
    liter = ""
    
    for i in lst:
        sums = sums + (i * binary)
        count += 1
        jug += 1
        if count == 4 or len(lst) == jug and len(lst) % 4 != 0 :    # 만일 4자리수가 모였거나, 자리수가 끝났을 경우 해당하는 값을 계산하여 반환하였습니다.
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

def octa_2(lst):                                                    # 8진수 2진수 변환
    num_list = []
    octa_list = []
    biny = ""
    count = 0    
    for num in lst:
        place_num = num
        for i in range(3):                                          # 1개의 숫자를 2진수 변환 형식으로 쪼개어 계산하였습니다.
            if place_num == 0:
                pass
            elif place_num == 1:
                octa_list.append(1)
                place_num = 0
                pass
            elif place_num % 2 == 1:
                place_num = (place_num - 1) / 2
                octa_list.append(1)
            else :
                place_num = place_num / 2
                octa_list.append(0)
            if len(octa_list) < 3 and place_num == 0:
                octa_list.append(0)
        num_list.extend(octa_list)
        octa_list.clear()
    num_list.reverse()
    
    for o in num_list :
        if num_list[0] == 0 :
            num_list.remove(0)
        else :
            break
            
    for i in num_list:
        biny = biny + str(i)

    return biny
    
def octa_10(lst):                                                   # 8진수 10진수 변환
    octa_place = 1
    result = 0
    
    for i in lst:
        result = result + (i * octa_place)
        octa_place = octa_place * 8
        
    return result

def octa_16(lst):                                                   # 8진수 16진수 변환
    octa_list_fir = []
    
    octa_fir = octa_2(lst)                                          # 8진수를 바로 16진수 변환은 할 수 없기 때문에 그 전에 사용했던 8진수 2진수 변환 함수를 사용합니다.
    
    for i in octa_fir:
        octa_list_fir.append(int(i))
        
    octa_list_fir.reverse()
    octa_sec = binary_16(octa_list_fir)                             # 2진수로 변환된 내용을 2진수 16진수 변환 함수를 활용하여 8진수 16진수 변환을 하였습니다.
                                                                    # 즉 8진수 -> 2진수 -> 16진수를 하였습니다.
    return octa_sec

def decimal_2(num):                                                 # 10진수 2진수 변환
    num_list = []
    biny = ""
    while True:
        if num == 0:
            num_list.reverse()
            break
        elif num == 1:
            num_list.append(1)
            num_list.reverse()
            break
        elif num % 2 == 1:
            num = (num - 1) / 2
            num_list.append(1)
        else :
            num = num / 2
            num_list.append(0)
    for i in num_list :
        biny = biny + str(i)

    return biny

def decimal_8(num):                                                 # 10진수 8진수 변환
    num_list = []
    octa = ""
    remainder = 0
    while True:
        if num < 8:
            num_list.append(int(num))
            num_list.reverse()
            break
        elif num == 8:
            num_list.append(0)
            num_list.append(1)
            num_list.reverse()
            break
        else:
            remainder = num % 8
            num = int(num - remainder) / 8
            num_list.append(int(remainder))
                        
    for i in num_list :
        octa = octa + str(i)
    
    return octa


def decimal_16(num):                                                # 10진수 16진수 변환
    num_list = []
    hexa = ""
    remainder = 0
    while True:
        if num < 16:
            if num == 10:
                liter = "A"
            elif num == 11:
                liter = "B"
            elif num == 12:
                liter = "C"
            elif num == 13:
                liter = "D"
            elif num == 14:
                liter = "E"
            elif num == 15:
                liter = "F"
            else :
                num_list.append(int(num))
            if num >= 10:
                num_list.append(str(liter))
            num_list.reverse()
            break
        elif num == 16:
            num_list.append(0)
            num_list.append(1)
            num_list.reverse()
            break
        else:
            remainder = num % 16
            if remainder == 10:
                liter = "A"
            elif remainder == 11:
                liter = "B"
            elif remainder == 12:
                liter = "C"
            elif remainder == 13:
                liter = "D"
            elif remainder == 14:
                liter = "E"
            elif remainder == 15:
                liter = "F"
            num = int(num - remainder) / 16
            if remainder >= 10:
                num_list.append(str(liter))
            else:
                num_list.append(int(remainder))
                
    for i in num_list :
        if num_list[0] == 0 :
            num_list.remove(0)
        else :
            break
    for i in num_list :
        hexa = hexa + str(i)

    return hexa

def hexa_2(lst):                                                    # 16진수 2진수 변환
    num_list = []
    hexa_list = []
    biny = ""
    count = 0    
    for num in lst:
        if (str(type(num)) == "<class 'int'>"):                     # 16진수는 알파벳도 들어가기 때문에 int가 맞는지 아닌지를 확인하였습니다.
            place_num = num
        elif num.upper() == "A":
            place_num = 10
        elif num.upper() == "B":
            place_num = 11
        elif num.upper() == "C":
            place_num = 12
        elif num.upper() == "D":
            place_num = 13
        elif num.upper() == "E":
            place_num = 14
        else:
            place_num = 15

        for i in range(4):                                          # 16진수 한 자리수는 2진수 4자리에 해당하기 때문에 range를 4로 하였습니다.
            if place_num == 0:
                pass
            elif place_num == 1:
                hexa_list.append(1)
                place_num = 0
                pass
            elif place_num % 2 == 1:
                place_num = (place_num - 1) / 2
                hexa_list.append(1)
            else :
                place_num = place_num / 2
                hexa_list.append(0)
            if len(hexa_list) < 4 and place_num == 0:
                hexa_list.append(0)
        num_list.extend(hexa_list)
        hexa_list.clear()
        
    num_list.reverse()
    
    for o in num_list :
        if num_list[0] == 0 :
            num_list.remove(0)
        else :
            break
            
    for i in num_list:
        biny = biny + str(i)

    return biny

def hexa_8(lst):                                                    # 16진수 8진수 변환
    hex_list_fir = []
    
    hexa_fir = hexa_2(lst)                                          # 16진수는 8진수로 바로 변환은 못하기 때문에 16진수에서 2진수 변환 함수를 사용하였습니다.
    
    for i in hexa_fir:
        hex_list_fir.append(int(i))
        
    hex_list_fir.reverse()
    hexa_sec = binary_8(hex_list_fir)                               # 2진수로 변환된 hex_list_fir를 2진수 8진수 변환로 8진수로 변환하였습니다.
                                                                    # 앞서 사용한 코드인 16진수 8진수 변환과 2진수 8진수 변환을 통하여 16진수를 8진수로 변환하였습니다.
    return hexa_sec                                                 # 16진수 -> 2진수 -> 8진수
    
def hexa_10(lst):                                                   # 16진수 10진수 변환
    hex_list_fir = []
    
    hexa_fir = hexa_2(lst)                                          # 16진수를 2진수로 변환
    
    for i in hexa_fir:
        hex_list_fir.append(int(i))
        
    hex_list_fir.reverse()
    hexa_sec = binary_10(hex_list_fir)                              # 2진수를 10진수로 변환
                                                                    # 16진수는 10진수로 바로 변환 가능하나, 위에 있는 함수를 호출하여 다시 재활용하는 것으로 구성하였습니다.
    return hexa_sec


while True:                 # 무한 루프로 구성하였습니다.
    try:
        jug = 0             # jug는 입력 값이 잘 못 입력되었을 경우 +1을 하고 반복문의 처음 부분으로 오도록 작성하였습니다.
        user_list = []      # user_list는 2진수, 8진수, 16진수 계산을 할 때 용이하게 하기 위해서 미리 선업하였습니다.
        print("(메뉴)\n\t11 (2진수 --> 8진수),\t12 (2진수 --> 10진수),\t13 (2진수 --> 16진수)\
        \n\t21 (8진수 --> 2진수),\t22 (8진수 --> 10진수),\t23 (8진수 --> 16진수)\
        \n\t31 (10진수 --> 2진수),\t32 (10진수 --> 8진수),\t33 (10진수 --> 16진수)\
        \n\t41 (16진수 --> 2진수),\t42 (16진수 --> 8진수),\t43 (16진수 --> 10진수)")
        user_in = input("메뉴선택 (1, 2, 3): ")
        if user_in == "":
            print("*" * 40)
            print("프로그램이 종료됩니다.")
            break
        else:
            user_num = input("입력 값(알파벳은 a~f까지): ")  # 만일 대문자로 입력하더라도 upper를 통해서 16진수 계산에 오류가 발생하지 않도록 구성하였습니다.
            if user_in[0] == "1":                    # user_in[0] 이 1 인 경우 2진수 이므로 2진수가 맞는지 확인하였습니다.
                if len(user_num) > 9:
                    print("범위 외의 값입니다.\n")
                    continue
                else:
                    for i in user_num:
                        if i == "1" or i == "0" :
                            user_list.append(int(i))
                        else :
                            print("-" * 25)
                            print("2진수가 아닙니다.")
                            print("-" * 25)
                            jug += 1
                            break
                    if jug == 1:
                        continue
                    for i in user_list :
                        if user_list[0] == 0 :
                            user_list.remove(0)
                        else :
                            break
                    user_list.reverse()
                    
                    if user_in == "11":
                        bin_8 = binary_8(user_list)
                        print("진수변환: %s (2진수) ---> %s (8진수)\n" % (user_num, bin_8))
                    elif user_in == "12":
                        bin_10 = binary_10(user_list)
                        print("진수변환: %s (2진수) ---> %s (10진수)\n" % (user_num, bin_10))
                    elif user_in == "13":
                        bin_16 = binary_16(user_list)
                        print("진수변환: %s (2진수) ---> %s (16진수)\n" % (user_num, bin_16))
                    else:
                        print("메뉴에 해당되지 않습니다.\n\n")
            elif user_in[0] == "2":             # user_in[0] 이 2 인 경우 8진수 이므로 8진수가 맞는지 확인하였습니다.
                if len(user_num) > 5:
                    print("범위 외의 값입니다.\n")
                else:
                    for i in user_num:
                        if int(i) < 8 :
                            user_list.append(int(i))
                        else :
                            print("-" * 25)
                            print("8진수가 아닙니다.")
                            print("-" * 25)
                            jug += 1
                            break
                    if jug == 1:
                        continue
                    for i in user_list :
                        if user_list[0] == 0 :
                            user_list.remove(0)
                        else :
                            break
                    user_list.reverse()
                    
                    if user_in == "21":
                        oct_2 = octa_2(user_list)
                        print("진수변환: %s (8진수) ---> %s (2진수)\n" % (user_num, oct_2))
                    elif user_in == "22":
                        oct_10 = octa_10(user_list)
                        print("진수변환: %s (8진수) ---> %s (10진수)\n" % (user_num, oct_10))
                    elif user_in == "23":
                        oct_16 = octa_16(user_list)
                        print("진수변환: %s (8진수) ---> %s (16진수)\n" % (user_num, oct_16))
            elif user_in[0] == "3":             
                if len(user_num) > 4:
                    print("범위 외의 값입니다.\n")
                else:
                    if user_in == "31":
                        dec_2 = decimal_2(int(user_num))
                        print("진수변환: %s (10진수) ---> %s (2진수)\n" % (user_num, dec_2))
                    elif user_in == "32":
                        dec_8 = decimal_8(int(user_num))
                        print("진수변환: %s (10진수) ---> %s (8진수)\n" % (user_num, dec_8))
                    elif user_in == "33":
                        dec_16 = decimal_16(int(user_num))
                        print("진수변환: %s (10진수) ---> %s (16진수)\n" % (user_num, dec_16))
            elif user_in[0] == "4":             # user_in[0] 이 4 인 경우 16진수 이므로 16진수가 맞는지 확인하였습니다.
                if len(user_num) > 3:
                    print("범위 외의 값입니다.\n")
                else:
                    for i in user_num:
                        if (i.upper() == "A" or i.upper() == "B" or i.upper() == "C" or
                        i.upper() == "D" or i.upper() == "E" or i.upper() == "F"):
                            user_list.append(str(i))
                            continue
                        elif int(i) < 10:
                            user_list.append(int(i))
                        else:
                            break
                    if jug == 1:
                        continue
                    for i in user_list :
                        if user_list[0] == 0 :
                            user_list.remove(0)
                        else :
                            break
                    user_list.reverse()
                    if user_in == "41":
                        hex_2 = hexa_2(user_list)
                        print("진수변환: %s (16진수) ---> %s (2진수)\n" % (user_num, hex_2))
                    elif user_in == "42":
                        hex_8 =hexa_8(user_list)
                        print("진수변환: %s (16진수) ---> %s (8진수)\n" % (user_num, hex_8))
                    elif user_in == "43":
                        hex_10 = hexa_10(user_list)
                        print("진수변환: %s (16진수) ---> %s (10진수)\n" % (user_num, hex_10))
            else:
                print("범위 이외의 값이나 문자가 입력되었습니다.\n\n")
        print("-" * 40)
    except ValueError:
        print("음수거나 문자, 실수가 입력되었습니다.\n처음부터 다시 시작합니다.\n\n")