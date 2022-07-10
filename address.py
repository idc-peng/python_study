# 주소록 만들기 1차 (전체를 리스트로 구성) / 2차는 다른 파일로 딕셔너리 예정
# 수정하는 중 11.06 시작 / 11.07 틀 완성(ui, 기본 함수) / 11.08 delete 함수 완성 / 11.09 part_lookup 함수 완성
# 11.17 메뉴 싹 다 갈아엎음.... (일찍 알았으면)
# 메뉴 6개로 추가 (a, v, s, sn, g, q) 범용 검색은 어떤건지 잘 모르겠음 + (g) 메뉴의 GUI는 뭔지 모름
# 신세계(ctrl + q) = 블럭 주석
# csv 파일을 할 때 쓰기함수에서 중요한 건 newline='' 인 것 같다. 쓰임은 말 그대로 newline인데 이는 파일을 읽고 마지막 위치에서 시작이 아닌 개행 후 시작을 뜻한다.
# 예외 처리를 안 한 이유는 input 받는 내용이 그나마 변수지만 내용상 string으로 받기 때문에 받는 데이터 오류의 여지가 없음. - 추가적으로 수정할 시 바뀔 수 있음
# modify 함수는 텍스트 필드 기준으로 제일 깔끔하게 만든듯 하지만 DB를 배울 경우 방식을 바꿔야만 함
# 현재 데이터를 끝날 때마다 오류처리를 하며 받는 변수는 전부 string이므로 오류는 힘듬
# 주석은 보기 편하게 달자. 습관!
# 일단 다음 내용 추가 전까진 20.11.19가 최종 버전

import csv

def add_data():                                             # 주소록 추가 함수
    c = open('book.csv','a', newline='')                    # "a" 로 내용수정
    c_writer = csv.writer(c)
    writer_list = []                                        # 쓰기 리스트
    jugNum = 0                                              # 판단 숫자
    
    user_name = input("추가할 사람의 이름을 입력하세요.\n입력 -> ")      # 이름대로 name, phone, email 순서
    user_phone_number = input("전화번호를 입력하세요. ex) 456-5678\n입력 -> ")
    user_email = input("이메일을 입력하세요.\n입력 -> ")
    
    if (user_name == "" or user_phone_number == "" or user_email == ""):    # 어떠한 요소라도 공란일 시 스킵 - 오타 경우를 넣음
        jugNum += 1
    
    if jugNum == 1:                                         # 공란일 시
        print("항목 중에 공란이 있어 추가되지 않았습니다.")
    else:                                                   # 아닐 시 writer_list에 내용을 구성
        writer_list.append("name= %s" % user_name)          # 리스트로 만들었기에 append
        writer_list.append("phone= %s" % user_phone_number)
        writer_list.append("email= %s" % user_email)
        
        c_writer.writerow(writer_list)                      # 구성한 내용을 한 행으로 추가
    
    c.close

def all_lookup():                                           # 전체 조회 함수
    f = open('book.csv', 'r')                               # "r"로 읽기
    f_reader = csv.reader(f)
    address_list = []                                       # 주소 담는 리스트
    
    for i in f_reader:                                      # csv 내용 address_list 에 저장
        address_list.append(i)
        
    print("   이름\t\t전화번호     이메일")                        # ui 구성용
        
    for x in range(len(address_list)):                      # len = csv파일 행 수
        for y in range(3):                                  # 3번 = name, phonenumber, email 3개 이므로 3번 루프(열 수)
            c = address_list[x][y]
            if address_list[x][y] == "":                    # 공란일 경우
                break
            elif y == 0:                                    # 'name= '을 슬라이싱
                print("%-12s" % c[6:], end = " /")          # 글자 왼쪽 정렬
            elif y == 1:                                    # 'phone= '을 슬라이싱
                print("%-10s" % c[7:], end = " /")
            else:                                           # 'email= '을 슬라이싱
                print("%-20s" % c[7:], end = "\n")
        print("-" * 40)
    print()
    
    f.close
    
def part_lookup():                                          # 부분(범용) 조회 함수 - 어떤 걸로 해야될지 몰라서 현재는 부분 조회 함수를 사용
    p = open('book.csv', 'r')                               # "r"로 읽기
    p_reader = csv.reader(p)
    address_list = []                                       # 주소 담는 리스트
    part_list = []                                          # 부분 리스트
    jugNum = 0
    
    user_serch_num = input("(메뉴)\n어떤 내용으로 찾으시겠습니까?\n\t1.이름\n\t2.전화번호\n\t3.이메일\n입력 -> ")      # 메뉴 구성
    
    for i in p_reader:                                      # address_list에 요소 넣기
        address_list.append(i)
    
    if user_serch_num == "":                                # 메뉴 엔터시
        print("엔터를 입력하셨기 때문에 처음 메뉴로 돌아갑니다.")
    elif user_serch_num == "1" or user_serch_num == "이름":   # 이름으로 조회할 경우
        user_serch = input("데이터의 이름을 입력하세요.\n-> ")
        for x in range(len(address_list)):                  # 행 수만큼 루프
            c = address_list[x][0]                          # [x행][0 = 첫째열 이므로 name]
            if user_serch.upper() == c[6:].upper():         # 'name= '슬라이싱
                part_list = (address_list[x])               # 해당 행을 part_list에 저장 (여기엔 name, phone, email을 포함한 행이 저장)
                break
    elif user_serch_num == "2" or user_serch_num == "전화번호": # 번호로 조회할 경우
        user_serch = input("데이터의 전화번호를 입력하세요.\n-> ")
        for x in range(len(address_list)):                  # 행 수만큼 루프
            c = address_list[x][1]                          # [x행][1 = 2열인 phone]
            if user_serch == c[7:]:                         # 'phone= '슬라이싱
                part_list = (address_list[x])               # 해당 행을 part_list에 저장 (여기엔 name, phone, email을 포함한 행이 저장)
                break
    elif user_serch_num == "3" or user_serch_num == "이메일":  # 이메일로 조회할 경우
        user_serch = input("데이터의 이메일을 입력하세요.\n-> ")
        for x in range(len(address_list)):                  # 행 수만큼 루프
            c = address_list[x][2]                          # [x행][2 = 3열인 email]
            if user_serch == c[7:]:                         # 'email= ' 슬라이싱
                part_list = (address_list[x])               # 해당 행을 part_list에 저장 (여기엔 name, phone, email을 포함한 행이 저장)
                break
    else:                                                   # 메뉴를 잘못 입력했을 경우
        print("메뉴에 해당되지 않습니다. 처음으로 돌아갑니다.")
    
    if len(part_list) == 0:
        print("주소록에 해당되지 않는 사람입니다.")
    else:
        print("   이름\t\t전화번호     이메일")                    # ui 구성용
        print("%-12s" % part_list[0][6:], end = " /")       # 글자 왼쪽 정렬로 출력, 슬라이싱 및 인덱싱 이용
        print("%-10s" % part_list[1][7:], end = " /")
        print("%-20s" % part_list[2][7:], end = "\n")
    
    print()
    print("-" * 40)
    
    p.close

def name_lookup():                                          # 이름 조회 함수 (부분 조회 함수의 일부분임)
    p = open('book.csv', 'r')                               # "r"로 읽기
    p_reader = csv.reader(p)
    address_list = []                                       # 주소 담는 리스트
    part_list = []                                          # 부분 리스트
    jugNum = 0
    
    for i in p_reader:                                      # address_list에 요소 넣기
        address_list.append(i)
    
    
    user_serch = input("데이터의 이름을 입력하세요.\n-> ")
    for x in range(len(address_list)):                      # 행 수만큼 루프
        c = address_list[x][0]                              # [x행][0 = 첫째열 이므로 name]
        if user_serch.upper() == c[6:].upper():             # 슬라이싱
            part_list = (address_list[x])                   # 해당 행을 part_list에 저장
            break
    
    if len(part_list) == 0:
        print("주소록에 해당되지 않는 사람입니다.")
    else:
        print("   이름\t\t전화번호     이메일")                    # ui 구성용
        print("%-12s" % part_list[0][6:], end = " /")       # 글자 왼쪽 정렬로 출력, 슬라이싱 및 인덱싱 이용
        print("%-10s" % part_list[1][7:], end = " /")
        print("%-20s" % part_list[2][7:], end = "\n")
    
    print()
    print("-" * 40)
    
    p.close
    
def modify():                                               # 수정 함수 - 이름으로 검색한 후 내용 수정임
    m = open('book.csv', 'r')                               # "r"로 읽기
    m_reader = csv.reader(m)
    address_list = []                                       # 주소 담는 리스트
    modify_list = []                                        # 변경 리스트
    writer_list = []                                        # 쓰기 리스트
    position_num = 0
    count = 0
    user_name = ""
    
    for i in m_reader:                                      # address_list에 요소 넣기
        address_list.append(i)

    user_serch = input("수정할 데이터의 이름을 입력하세요.\n-> ")       # 이름을 확인 
    for x in range(len(address_list)):                      # 행 수만큼 루프
        c = address_list[x][0]                              # [x행][0 = 첫째열 이므로 name]
        if user_serch.upper() == c[6:].upper():             # 슬라이싱 사용, upper을 통하여 대소문자 상관없이 구성
            user_name = input("수정할 사람의 이름을 입력하세요.\n입력 -> ") # 이름대로 name, phone, email 순서
            user_phone_number = input("전화번호를 입력하세요. ex) 456-5678\n입력 -> ")
            user_email = input("이메일을 입력하세요.\n입력 -> ")
            print("수정되었습니다.")                              # 수정되었다고 알림으로 표시
            position_num = x                                # address_list에 해당 행을 삭제
            m.close
            break
            
    if user_name == "":                                     # 데이터가 해당된 자료가 없는 경우
        print("앗 자료가 없군요!")
    else:    
        modify_list.append("name= %s" % user_name)          # 수정 리스트에 추가 함수와 비슷하게 내용 추가
        modify_list.append("phone= %s" % user_phone_number)
        modify_list.append("email= %s" % user_email)
    
        # address_list.append(modify_list)                  # 이걸 추가하고 밑에 조건문을 없앨 경우 수정은 되지만 수정된 자료가 제일 밑으로 내려감
    
        e = open('book.csv', 'w', newline='')               # 'w'로 쓰기함수 (쓰기함수 사용할 경우 csv파일 내용이 포맷되는 것을 이용)
        e_writer = csv.writer(e)
        
        for i in address_list:                              # address_list의 len은 행 수이므로 삭제되고 남은 행만큼 루프
            writer_list.append(i[0])                        # name 부분
            writer_list.append(i[1])                        # phone 부분
            writer_list.append(i[2])                        # email 부분
            
            if position_num == count:
                e_writer.writerow(modify_list)
            else:
                e_writer.writerow(writer_list)              # writerow로 행에 내용 추가
            
            writer_list.clear()
            count += 1
    
        print()
        print("-" * 40)
    
        e.close

# 삭제 함수는 현재는 제거 상태이다. 물론 작동은 진~~~짜 잘한다. (교수님도 되긴 한다고 함.) 다만 이 방식을 안 쓰는 이유는 되긴 하지만 좋지 못한 방식이기 때문이다.
# 누가 자료를 저장할 때 있는 내용을 전부 리셋하고 리셋 전 데이터를 복구를 하는가. 나중에 DB를 사용할 때 배우자!! 텍스트 파일이므로 이 방법이 옳은 방법은 맞다. (메뉴에 없어서 지움)
   
# def delete_data():                          # 삭제 함수
    # d = open('book.csv', 'r')               # 'r'로 읽기
    # d_reader = csv.reader(d)
    # address_list = []                       # 주소 리스트
    # writer_list = []                        # 쓰기 리스트
    
    # print()
    # print("-" * 40)
    # user_serch_num = input("(메뉴)\n삭제할 데이터를 어떤 내용으로 찾으시겠습니까?\n\t1.이름\n\t2.전화번호\n\t3.이메일\
                            # \n입력 -> ")      # 메뉴 구성
    
    # for i in d_reader:                      # address_list에 요소 넣기
        # address_list.append(i)
    
    # if user_serch_num == "":                # 메뉴 엔터시
        # print("엔터를 입력하셨기 때문에 처음 메뉴로 돌아갑니다.")
    # elif user_serch_num == "1" or user_serch_num == "이름":   # 이름으로 삭제할 경우
        # user_serch = input("삭제할 데이터의 이름을 입력하세요.\n-> ")
        # for x in range(len(address_list)):  # 행 수만큼 루프
            # c = address_list[x][0]          # [x행][0 = 첫째열 이므로 name]
            # if user_serch.upper() == c[6:].upper():         # 슬라이싱 사용, upper을 통하여 대소문자 상관없이 구성
                # repeat = input("정말로 삭제하시겠습니까?\n삭제를 원하시면 '네' 를 입력하세요.")  # 삭제 확인
                # if repeat == "네":           # '네' 입력시
                    # print("삭제되었습니다.")      # 삭제되었다고 알림
                    # del address_list[x]     # address_list에 해당 행을 삭제
                    # d.close
                # break
    # elif user_serch_num == "2" or user_serch_num == "전화번호": # 번호로 삭제할 경우
        # user_serch = input("삭제할 데이터의 전화번호를 입력하세요.\n-> ")
        # for x in range(len(address_list)):  # 행 수
            # c = address_list[x][1]          # [x행][1열 = phone]
            # if user_serch == c[7:]:         # 슬라이싱 사용, upper을 통하여 대소문자 상관없이 구성
                # repeat = input("정말로 삭제하시겠습니까?\n삭제를 원하시면 '네' 를 입력하세요.")
                # if repeat == "네":           # 삭제 확인
                    # print("삭제되었습니다.")
                    # del address_list[x]     # address_list에 해당 행을 삭제
                    # d.close
                # break
    # elif user_serch_num == "3" or user_serch_num == "이메일":  # 이메일로 삭제할 경우
        # user_serch = input("삭제할 데이터의 이메일을 입력하세요.\n-> ")
        # for x in range(len(address_list)):  # 행 수
            # c = address_list[x][2]          # [x행][2열 = email]
            # if user_serch == c[7:]:         # 슬라이싱 사용, upper을 통하여 대소문자 상관없이 구성
                # repeat = input("정말로 삭제하시겠습니까?\n삭제를 원하시면 '네' 를 입력하세요.")
                # if repeat == "네":           # 삭제 확인
                    # print("삭제되었습니다.")
                    # del address_list[x]     # address_list에 해당 행을 삭제
                    # d.close
                # break
    # else:                                   # 메뉴를 잘못 입력했을 경우
        # print("메뉴에 해당되지 않습니다. 처음으로 돌아갑니다.")
        
    # e = open('book.csv', 'w', newline='')   # 'w'로 쓰기함수 (쓰기함수 사용할 경우 csv파일 내용이 포맷되는 것을 이용)
    # e_writer = csv.writer(e)
        
    # for i in address_list:                  # address_list의 len은 행 수이므로 삭제되고 남은 행만큼 루프
        # writer_list.append(i[0])            # name 부분
        # writer_list.append(i[1])            # phone 부분
        # writer_list.append(i[2])            # email 부분
        
        # e_writer.writerow(writer_list)      # writerow로 행에 내용 추가
        # writer_list.clear()                 # writer_list를 clear를 하여 초기화
        
    # e.close

while True:                                                 # main
    print("*" * 40)
    user_in = input("(메뉴)\n\n\t(a)\t새 전화번호 추가\n\t(v)\t전체 전화번호 출력\n\t(s)\t범용 검색\
                    \n\t(sn)\t이름으로 검색\n\t(g)\t이름 검색 및 수정 (GUI)\
                    \n\t(q)\t종료\n\n입력란 : ")                # 메뉴 구성
    if user_in == "a":                                      # 추가
        add_data()
    elif user_in == "v":                                    # 전체 조회
        all_lookup()
    elif user_in == "s":                                    # 범용(현재는 부분) 조회
        part_lookup()
    elif user_in == "sn":                                   # 이름 조회
        name_lookup()
    elif user_in == "g":                                    # 이름으로 검색 및 수정
        modify()
    elif user_in == "q":                                    # 종료
        break
    else:                                                   # 해당되는 메뉴가 없을 시
        print("메뉴에 해당하지 않는 내용입니다.")