# 진수 구하기

import csv

def binary():
    f = open('in_data.csv', 'r')
    c = open('out_data.txt', 'w')
    a = csv.reader(f)
    num_list = []
    biny = ""
    count = 0
    bin_num = 0
    org_num = 0
    
    for i in a:
        for x in range(20):
            try:
                if x == 0:
                    lis = i
                while True:
                    if count == 0:
                        bin_num = int(lis[x])
                        org_num = lis[x]
                        count += 1
                    elif int(org_num) > 9999:
                        print("범위을 벗어났습니다.")
                        break
                    else:
                        if bin_num == 0:
                            num_list.reverse()
                            break
                        elif bin_num == 1:
                            num_list.append(1)
                            num_list.reverse()
                            break
                        elif bin_num % 2 == 1:
                            bin_num = (bin_num - 1) / 2
                            num_list.append(1)
                        else :
                            bin_num = bin_num / 2
                            num_list.append(0)
                for i in num_list :
                    biny = biny + str(i)
                print("진수변환: %s (10진수) ---> %s (2진수)\n" % (org_num, biny))
                print("-" * 40)
                if x == 0:
                    c.write("진수변환: %s (10진수) ---> %s (2진수)\n" % (org_num, biny))
                    c.write("-" * 50)
                elif x == 7:
                    c.write("\n진수변환: %s (10진수) ---> %s (2진수)\n" % (org_num, biny))
                else:   
                    c.write("\n진수변환: %s (10진수) ---> %s (2진수)\n" % (org_num, biny))
                    c.write("-" * 50)
                num_list.clear()
                count = 0
                biny = ""
            except IndexError:
                break
    f.close

def octal():
    f = open('in_data.csv', 'r')
    c = open('out_data.txt', 'w')
    a = csv.reader(f)
    num_list = []
    octa = ""
    count = 0
    remainder = 0
    org_num = 0
    octa_num = 0
    
    for i in a:
        for x in range(20):
            try:
                if x == 0:
                    lis = i
                while True:
                    if count == 0:
                        octa_num = int(lis[x])
                        org_num = lis[x]
                        count += 1
                    elif int(org_num) > 9999:
                        print("범위을 벗어났습니다.")
                        break
                    else:
                        if octa_num < 8:
                            num_list.append(int(octa_num))
                            num_list.reverse()
                            break
                        elif octa_num == 8:
                            num_list.append(0)
                            num_list.append(1)
                            num_list.reverse()
                            break
                        else:
                            remainder = octa_num % 8
                            octa_num = int(octa_num - remainder) / 8
                            num_list.append(int(remainder))
                        
                for i in num_list :
                    octa = octa + str(i)
                print("진수변환: %s (10진수) ---> %s (8진수)\n" % (org_num, octa))
                print("-" * 40)
                if x == 0:
                    c.write("진수변환: %s (10진수) ---> %s (8진수)\n" % (org_num, octa))
                    c.write("-" * 50)
                elif x == 7:
                    c.write("\n진수변환: %s (10진수) ---> %s (8진수)\n" % (org_num, octa))
                else:
                    c.write("\n진수변환: %s (10진수) ---> %s (8진수)\n" % (org_num, octa))
                    c.write("-" * 50)
                num_list.clear()
                count = 0
                octa = ""
            except IndexError:
                break
    f.close
    
def hexa():
    f = open('in_data.csv', 'r')
    c = open('out_data.txt', 'w')
    a = csv.reader(f)
    num_list = []
    hexa = ""
    count = 0
    remainder = 0
    org_num = 0
    hexa_num = 0
    liter = ""
    for i in a:
        for x in range(20):
            try:
                if x == 0:
                    lis = i
                while True:
                    if count == 0:
                        hexa_num = int(lis[x])
                        org_num = lis[x]
                        count += 1
                    elif int(org_num) > 9999:
                        print("범위을 벗어났습니다.")
                        break
                    else:
                        if hexa_num < 16:
                            if hexa_num == 10:
                                liter = "A"
                            elif hexa_num == 11:
                                liter = "B"
                            elif hexa_num == 12:
                                liter = "C"
                            elif hexa_num == 13:
                                liter = "D"
                            elif hexa_num == 14:
                                liter = "E"
                            elif hexa_num == 15:
                                liter = "F"
                            else :
                                num_list.append(int(hexa_num))
                            num_list.reverse()
                            break
                        elif hexa_num == 16:
                            num_list.append(0)
                            num_list.append(1)
                            num_list.reverse()
                            break
                        else:
                            remainder = hexa_num % 16
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
                            hexa_num = int(hexa_num - remainder) / 16
                            if remainder >= 10:
                                num_list.append(liter)
                            else:
                                num_list.append(int(remainder))
                
                for i in num_list :
                    hexa = hexa + str(i)
                
                print("진수변환: %s (10진수) ---> %s (16진수)\n" % (org_num, hexa))
                print("-" * 40)
                if x == 0:
                    c.write("진수변환: %s (10진수) ---> %s (16진수)\n" % (org_num, hexa))
                    c.write("-" * 50)
                elif x == 7:
                    c.write("\n진수변환: %s (10진수) ---> %s (16진수)\n" % (org_num, hexa))
                else:
                    c.write("\n진수변환: %s (10진수) ---> %s (16진수)\n" % (org_num, hexa))
                    c.write("-" * 50)
                num_list.clear()
                count = 0
                hexa = ""
            except IndexError:
                break
    f.close
    
while True:
    try:
        print("(메뉴)\n")
        print("\t1 : 10진수 --> 2진수 변환\n\t2 : 10진수 --> 8진수 변환\n\t3 : 10진수 --> 16진수 변환\n")
        user_in = input("메뉴선택 (1, 2, 3) :")
        
        if user_in == "":
            print("*" * 40)
            print("\n프로그램을 종료합니다.")
            break
        
        if user_in == "1":
            binary()
        elif user_in == "2":
            octal()
        elif user_in == "3":
            hexa()
        else:
            print("-" * 40)
            print("\n메뉴에 해당되지 않습니다.\n")
            print("-" * 40)
    except ValueError:
        print("입력값이 잘못 입력되었습니다.")