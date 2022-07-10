# 약수 구하기 4탄 메모장 이용하기

import csv

def div():
    f = open("in_data.csv", 'r')    # in_data.csv 'r'(읽기전용)
    c = open("out_data.txt", 'w')   # out_data.txt 'w'(쓰기전용)
    a = csv.reader(f)
    div_num = 0
    
    for i in a:
        for x in range(20):
            try:
                if x == 0:
                    lis = i
                while True:
                    try:
                        div_num = int(lis[x])
                        count = 0
                        print(div_num, "의 약수는 -> ", end = "")
                        c.write("\n%d 의 약수는 -> " % div_num)
                        for y in range(1, div_num+1):
                            if div_num % y == 0:
                                if div_num == y :
                                    print(y, end = " ")
                                    c.write("%d" % y)
                                    count += 1
                                else :
                                    print(y, end = ", ")
                                    c.write("%d, " % y)
                                    count += 1
                        print()
                        print("약수의 개수는 -> %d 개" % count)
                        c.write("\n약수의 개수는 -> %d 개\n" % count)
                        c.write("-" * 25)
                        print("-" * 40)
                        f.close
                        break
                    except ValueError:             # 메모장에서 int(lis[x])으로 변환할 수 없는 경우가 해당됩니다.
                        if lis[x] == "":             # 메모장의 f.readline()의 마지막은 ""이므로 정상적으로 끝났을 경우입니다.
                            print("종료되었습니다.")
                            f.close
                            break
                        elif lis[x] == "\n":         # 만약 개행일 시 다시 실행
                            continue
                        else:                      # 만약 ""로 종료가 안 됬을 경우에는 int(lis[x])이 안되는 실수나 문자가 입력된 것이므로
                            print("*" * 40)        # 프로그램을 종료시킵니다.
                            print("파일 내용을 수정해야합니다.")
                            print("*" * 40)
                            return 'Error'         # return에 'Error'를 반환하였습니다.
            except IndexError:
                break

while True :
    print("\ncsv파일에 입력된 정수의 약수를 구하는 프로그램입니다.\n")
    print("-" * 40)
    user_in = input("어떤 것을 하시겠습니까??\n(실행 : 1 | 종료 : Enter)\n입력란 ->")
    print("*" * 50)
    if user_in == "1" :
        a = div()
        if a == "Error" :                  # 함수의 반환값이 Error일 시 break를 하여 프로그램을 종료합니다.
            break
    elif user_in == "" :
        print("프로그램이 종료되었습니다.")
        break
    else:
        print("해당되지 않습니다. 다시 입력해 주십시오.")