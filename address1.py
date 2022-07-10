# 주소록 만들기 2차 (DictReader 사용)
# csv 파일 읽을 때 문자가 깨지면 encoding을 염두하자! encoding='utf-8-sig'
# 시작일 - 20.11.15 , all_lookup에서 리스트로 받는게 아닌 딕셔너리로 받아볼려 했으나 아직 연습 필요함.
# 20.11.18 새로 알게된 사실 - range 함수는 당연히 역순도 가능한 건 알았지만 음수가 되는건 진짜 처음 알았다. ex) range(-2, 1) / range(10, -5, -1)
#                                                                                                       부터  까지  증감

import csv

def all_lookup():                                           # 전체 조회 함수
    f = open('book_ex.csv', 'r', encoding='utf-8-sig')      # "r"로 읽기
    f_reader = csv.DictReader(f)
    address_list = []                                       # 주소 담는 리스트
    count = 0
    
    for i in f_reader:                                      # csv 내용 address_list 에 저장
        address_list.append(i['name'])
        address_list.append(i['phone'])
        address_list.append(i['email'])
    
    print("     이름\t전화번호     이메일")                        # ui 구성용
        
    for x in range(len(address_list)):                      # len = csv파일 행 수
        if address_list[x] == "":                           # 공란일 경우
                break
        else:                                               # name= 을 슬라이싱
            print("%-12s" % address_list[count], end = "")  # 글자 왼쪽 정렬
               
        if x % 3 == 2:
            print("\n")
            print("-" * 40)
        else:
            print(end = " /")
        count += 1
    print()
    
    f.close
    
def part_lookup():                                          # 부분 조회 함수
    p = open('book_ex.csv', 'r', encoding='utf-8-sig')      # "r"로 읽기
    p_reader = csv.DictReader(p)
    address_list = []                                       # 주소 담는 리스트
    part_list = []
    jugNum = 0
    
    user_serch_num = input("(메뉴)\n어떤 내용으로 찾으시겠습니까?\n\t1.이름\n\t2.전화번호\n\t3.이메일\n입력 -> ")      # 메뉴 구성
    
    for i in p_reader:                                      # csv 내용 address_list 에 저장
        address_list.append(i['name'])
        address_list.append(i['phone'])
        address_list.append(i['email'])
    
    if user_serch_num == "":                                # 메뉴 엔터시
        print("엔터를 입력하셨기 때문에 처음 메뉴로 돌아갑니다.")
    elif user_serch_num == "1" or user_serch_num == "이름":   # 이름으로 조회할 경우
        user_serch = input("데이터의 이름을 입력하세요.\n-> ")
        for x in range(len(address_list)):                  # 행 수만큼 루프
            c = address_list[x]                             # [x행][0 = 첫째열 이므로 name]
            if user_serch.upper() == c.upper():             # 슬라이싱
                for j in range(3):
                    part_list.append(address_list[x + j])   # 해당 행을 part_list에 저장
                break
    elif user_serch_num == "2" or user_serch_num == "전화번호": # 번호로 조회할 경우
        user_serch = input("데이터의 전화번호를 입력하세요.\n-> ")
        for x in range(len(address_list)):                  # 행 수
            c = address_list[x]                             # [x행][1열 = phone]
            if user_serch == c:                             # 슬라이싱
                for j in range(-1, 2):
                    part_list.append(address_list[x + j])   # 해당 행을 part_list에 저장
                break
    elif user_serch_num == "3" or user_serch_num == "이메일":  # 이메일로 조회할 경우
        user_serch = input("데이터의 이메일을 입력하세요.\n-> ")
        for x in range(len(address_list)):                  # 행 수
            c = address_list[x]                             # [x행][2열 = email]
            if user_serch == c:                             # 슬라이싱
                for j in range(-2, 1):
                    part_list.append(address_list[x + j])   # 해당 행을 part_list에 저장
                break
    else:                                                   # 메뉴를 잘못 입력했을 경우
        print("메뉴에 해당되지 않습니다. 처음으로 돌아갑니다.")
    
    for i in part_list:
        print(i)
    
    if len(part_list) == 0:
        print("주소록에 해당되지 않는 사람입니다.")
    else:
        print("   이름\t\t전화번호     이메일")                    # ui 구성용
        print("%-12s" % part_list[0], end = " /")           # 글자 왼쪽 정렬로 출력, 슬라이싱 및 인덱싱 이용
        print("%-10s" % part_list[1], end = " /")
        print("%-20s" % part_list[2], end = "\n")
    
    print()
    print("-" * 40)
    
    p.close
    

def add_data():                                             # 추가 함수
    c = open('book_ex.csv','a', newline='', encoding='utf-8-sig')    # "a" 로 내용수정
    c_writer = csv.writer(c)
    writer_dict = {}                                        # 쓰기 딕셔너리(사전)
    jugNum = 0                                              # 판단 숫자
    
    user_name = input("추가할 사람의 이름을 입력하세요.\n입력 -> ")      # 이름대로 name, phone, email 순서
    user_phone_number = input("전화번호를 입력하세요. ex) 456-5678\n입력 -> ")
    user_email = input("이메일을 입력하세요.\n입력 -> ")
    
    if (user_name == "" or user_phone_number == "" or user_email == ""):    # 공란일 시 스킵
        jugNum += 1
           
    if jugNum == 1:                                         # 공란일 시
        print("항목 중에 공란이 있어 추가되지 않았습니다.")
    else:                                                   # 아닐 시 writer_dict 내용을 구성
        writer_dict['name'] = user_name
        writer_dict['phone'] = user_phone_number
        writer_dict['email'] = user_email
        
        c_writer.writerow(writer_dict.values())             # 구성한 내용을 한 행으로 추가
    
    c.close
    
def delete_data():                                          # 삭제 함수
    d = open('book_ex.csv', 'r', encoding='utf-8-sig')      # 'r'로 읽기
    d_reader = csv.reader(d)
    address_list = []                                       # 주소 리스트
    writer_list = []                                        # 쓰기 리스트
    
    print()
    print("-" * 40)
    user_serch_num = input("(메뉴)\n삭제할 데이터를 어떤 내용으로 찾으시겠습니까?\n\t1.이름\n\t2.전화번호\n\t3.이메일\
                            \n입력 -> ")                      # 메뉴 구성
    
    for i in d_reader:                                      # address_list에 요소 넣기
        address_list.append(i)
    
    if user_serch_num == "":                                # 메뉴 엔터시
        print("엔터를 입력하셨기 때문에 처음 메뉴로 돌아갑니다.")
    elif user_serch_num == "1" or user_serch_num == "이름":   # 이름으로 삭제할 경우
        user_serch = input("삭제할 데이터의 이름을 입력하세요.\n-> ")
        for x in range(len(address_list)):                  # 행 수만큼 루프
            c = address_list[x][0]                          # [x행][0 = 첫째열 이므로 name]
            if user_serch.upper() == c.upper():             # 슬라이싱
                repeat = input("정말로 삭제하시겠습니까?\n삭제를 원하시면 '네' 를 입력하세요.")  # 삭제 확인
                if repeat == "네":                           # '네' 입력시
                    print("삭제되었습니다.")                      # 삭제되었다고 알림
                    del address_list[x]                     # address_list에 해당 행을 삭제
                    d.close
                break
    elif user_serch_num == "2" or user_serch_num == "전화번호": # 번호로 삭제할 경우
        user_serch = input("삭제할 데이터의 전화번호를 입력하세요.\n-> ")
        for x in range(len(address_list)):                  # 행 수
            c = address_list[x][1]                          # [x행][1열 = phone]
            if user_serch == c:                             # 슬라이싱
                repeat = input("정말로 삭제하시겠습니까?\n삭제를 원하시면 '네' 를 입력하세요.")
                if repeat == "네":                           # 삭제 확인
                    print("삭제되었습니다.")
                    del address_list[x]                     # address_list에 해당 행을 삭제
                    d.close
                break
    elif user_serch_num == "3" or user_serch_num == "이메일":  # 이메일로 삭제할 경우
        user_serch = input("삭제할 데이터의 이메일을 입력하세요.\n-> ")
        for x in range(len(address_list)):                  # 행 수
            c = address_list[x][2]                          # [x행][2열 = email]
            if user_serch == c:                             # 슬라이싱
                repeat = input("정말로 삭제하시겠습니까?\n삭제를 원하시면 '네' 를 입력하세요.")
                if repeat == "네":                           # 삭제 확인
                    print("삭제되었습니다.")
                    del address_list[x]                     # address_list에 해당 행을 삭제
                    d.close
                break
    else:                                                   # 메뉴를 잘못 입력했을 경우
        print("메뉴에 해당되지 않습니다. 처음으로 돌아갑니다.")
        
    e = open('book.csv', 'w', newline='')                   # 'w'로 쓰기함수 (쓰기함수 사용할 경우 csv파일 내용이 포맷되는 것을 이용)
    e_writer = csv.writer(e)
        
    for i in address_list:                                  # address_list의 len은 행 수이므로 삭제되고 남은 행만큼 루프
        writer_list.append(i[0])                            # name 부분
        writer_list.append(i[1])                            # phone 부분
        writer_list.append(i[2])                            # email 부분
        
        e_writer.writerow(writer_list)                      # writerow로 행에 내용 추가
        writer_list.clear()                                 # writer_list를 clear를 하여 초기화
        
    e.close

while True:                                                 # main
    print("*" * 40)
    user_in = input("(메뉴)\n\n\t1.전체조회 -> 1\n\t2.부분조회 -> 2\n\t3.추가 -> 3\n\t4.삭제 -> 4\n\n입력란 : ")  # 메뉴 구성
    
    if user_in == "1" or user_in == "전체조회":                 # 전체 조회
        all_lookup()
    elif user_in == "2" or user_in == "부분조회":               # 부분 조회
        part_lookup()
    elif user_in == "3" or user_in == "추가":                 # 추가
        add_data()
    elif user_in == "4" or user_in == "삭제":                 # 삭제
        delete_data()
    elif user_in == "":     # 엔터 시
        break
    else:                                                   # 해당되는 메뉴가 없을 시
        print("메뉴에 해당하지 않는 내용입니다.")