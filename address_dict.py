# 주소록 만들기 2차 (DictReader 사용)
# 시작일 - 20.11.15 , all_lookup에서 리스트로 받는게 아닌 딕셔너리로 받아볼려 했으나 아직 연습 필요함.
# 놀라운 사실을 알아냄.. 20.11.17~8 일단 원래 딕셔너리 키 값이 중복이 안 되는데 어떻게 하는지 진짜 아예 몰랐고 현재도 잘 모름
# 하지만 알아낸 사실은 키 값을 중복으로 받을 수 있다는 사실도 알게됬는데 어이없는건 그래봤자 리스트로 변환해서 받아야해서 힘들기만하고 쓸데없음
# 파일 이름은 'book_ex.csv'를 통해서 하고있다. 이유는 DictReader는 key를 무조건 첫 행을 key값으로 잡는다. 즉 목록이 위에 있어야만 가능

import csv

# class person(object):             # 웹 서칭해서 찾은 고마우신 코드
    # def __init__(self,name):      # 일반적으로 딕셔너리를 키 값이 중복이 불가능하다!!
        # self.name = name          # 하지만 키 값을 각각의 객체로 해주는 class인 person을 쓸 경우 가능함
                                
    # def __str__(self):            # 분석을 못하겠다...
        # return self.name

    # def __repr__(self):
        # return "'"+self.name+"'"

def all_lookup():                           # 전체 조회 함수
    f = open('book_ex.csv', 'r', encoding='utf-8-sig')      # "r"로 읽기
    f_reader = csv.DictReader(f)
    address_list = []                       # 주소 담는 리스트
    address_dict = {}
    count = 0
    
    for i in f_reader:                      # csv 내용 address_list 에 저장
        address_list.append(i['name'])
        address_list.append(i['phone'])
        address_list.append(i['email'])

    # f.close           # 완전 딕셔너리에서 전부 딕셔너리로 받은 후 바꾸는 코드임....
                        # 문제는 이래봤자 리스트로 변환해서 요소를 넣는 건데 의미가 있나...?
                        # 나중에 수정할 경우엔 딕셔너리로만 전부 하겠지만 효율이 너무 떨어짐. 라인이 너무 길어지고 복잡해짐.
                        # 일단 이 방식을 이용하면 전부 고칠 수 있다! 하지만 다른 걸로 딕셔너리 공부하는게 훨씬 좋아보임
    # m = open('book_ex.csv', 'r', encoding='utf-8-sig')
    # m_reader = csv.DictReader(m)
    
    # for i in m_reader:
        # for k, v in i.items():
            # address_dict[person(k)] = v
            
    # b = list(address_dict.values())
    
    # print(b)
    
    print("     이름\t전화번호     이메일")        # ui 구성용
        
    for x in range(len(address_list)):      # len = csv파일 행 수
        if address_list[x] == "":    # 공란일 경우
                break
        else:                    # name= 을 슬라이싱
            print("%-12s" % address_list[count], end = "")  # 글자 왼쪽 정렬
               
        if x % 3 == 2:
            print("\n")
            print("-" * 40)
        else:
            print(end = " /")
        count += 1
    print()
    
    f.close
    
def part_lookup():                          # 부분 조회 함수
    p = open('book_ex.csv', 'r')               # "r"로 읽기
    p_reader = csv.reader(p)
    address_list = []                       # 주소 담는 리스트
    part_list = []
    jugNum = 0
    
    user_serch_num = input("(메뉴)\n어떤 내용으로 찾으시겠습니까?\n\t1.이름\n\t2.전화번호\n\t3.이메일\n입력 -> ")      # 메뉴 구성
    
    for i in p_reader:                      # address_list에 요소 넣기
        address_list.append(i)
    
    if user_serch_num == "":                # 메뉴 엔터시
        print("엔터를 입력하셨기 때문에 처음 메뉴로 돌아갑니다.")
    elif user_serch_num == "1" or user_serch_num == "이름":   # 이름으로 조회할 경우
        user_serch = input("데이터의 이름을 입력하세요.\n-> ")
        for x in range(len(address_list)):  # 행 수만큼 루프
            c = address_list[x][0]          # [x행][0 = 첫째열 이므로 name]
            if user_serch.upper() == c.upper():         # 슬라이싱
                part_list = (address_list[x])               # 해당 행을 part_list에 저장
                break
    elif user_serch_num == "2" or user_serch_num == "전화번호": # 번호로 조회할 경우
        user_serch = input("데이터의 전화번호를 입력하세요.\n-> ")
        for x in range(len(address_list)):  # 행 수
            c = address_list[x][1]          # [x행][1열 = phone]
            if user_serch == c:         # 슬라이싱
                part_list = (address_list[x])               # 해당 행을 part_list에 저장
                break
    elif user_serch_num == "3" or user_serch_num == "이메일":  # 이메일로 조회할 경우
        user_serch = input("데이터의 이메일을 입력하세요.\n-> ")
        for x in range(len(address_list)):  # 행 수
            c = address_list[x][2]          # [x행][2열 = email]
            if user_serch == c:         # 슬라이싱
                part_list = (address_list[x])               # 해당 행을 part_list에 저장
                break
    else:                                   # 메뉴를 잘못 입력했을 경우
        print("메뉴에 해당되지 않습니다. 처음으로 돌아갑니다.")
    
    if len(part_list) == 0:
        print("주소록에 해당되지 않는 사람입니다.")
    else:
        print("   이름\t\t전화번호     이메일")               # ui 구성용
        print("%-12s" % part_list[0], end = " /")  # 글자 왼쪽 정렬로 출력, 슬라이싱 및 인덱싱 이용
        print("%-10s" % part_list[1], end = " /")
        print("%-20s" % part_list[2], end = "\n")
    
    print()
    print("-" * 40)
    
    p.close
    

def add_data():                             # 추가 함수
    c = open('book_ex.csv','a', newline='')    # "a" 로 내용수정
    c_writer = csv.writer(c)
    writer_list = []                        # 쓰기 리스트
    jugNum = 0                              # 판단 숫자
    
    user_name = input("추가할 사람의 이름을 입력하세요.\n입력 -> ") # 이름대로 name, phone, email 순서
    user_phone_number = input("전화번호를 입력하세요. ex) 456-5678\n입력 -> ")
    user_email = input("이메일을 입력하세요.\n입력 -> ")
    
    if (user_name == "" or user_phone_number == "" or user_email == ""):    # 공란일 시 스킵
        jugNum += 1
    
    if jugNum == 1:                         # 공란일 시
        print("항목 중에 공란이 있어 추가되지 않았습니다.")
    else:                                   # 아닐 시 writer_list에 내용을 구성
        writer_list.append("%s" % user_name)
        writer_list.append("%s" % user_phone_number)
        writer_list.append("%s" % user_email)
        
        c_writer.writerow(writer_list)      # 구성한 내용을 한 행으로 추가
    
    c.close
    
def delete_data():                          # 삭제 함수
    d = open('book_ex.csv', 'r')               # 'r'로 읽기
    d_reader = csv.reader(d)
    address_list = []                       # 주소 리스트
    writer_list = []                        # 쓰기 리스트
    
    print()
    print("-" * 40)
    user_serch_num = input("(메뉴)\n삭제할 데이터를 어떤 내용으로 찾으시겠습니까?\n\t1.이름\n\t2.전화번호\n\t3.이메일\
                            \n입력 -> ")      # 메뉴 구성
    
    for i in d_reader:                      # address_list에 요소 넣기
        address_list.append(i)
    
    if user_serch_num == "":                # 메뉴 엔터시
        print("엔터를 입력하셨기 때문에 처음 메뉴로 돌아갑니다.")
    elif user_serch_num == "1" or user_serch_num == "이름":   # 이름으로 삭제할 경우
        user_serch = input("삭제할 데이터의 이름을 입력하세요.\n-> ")
        for x in range(len(address_list)):  # 행 수만큼 루프
            c = address_list[x][0]          # [x행][0 = 첫째열 이므로 name]
            if user_serch.upper() == c.upper():         # 슬라이싱
                repeat = input("정말로 삭제하시겠습니까?\n삭제를 원하시면 '네' 를 입력하세요.")  # 삭제 확인
                if repeat == "네":           # '네' 입력시
                    print("삭제되었습니다.")      # 삭제되었다고 알림
                    del address_list[x]     # address_list에 해당 행을 삭제
                    d.close
                break
    elif user_serch_num == "2" or user_serch_num == "전화번호": # 번호로 삭제할 경우
        user_serch = input("삭제할 데이터의 전화번호를 입력하세요.\n-> ")
        for x in range(len(address_list)):  # 행 수
            c = address_list[x][1]          # [x행][1열 = phone]
            if user_serch == c:         # 슬라이싱
                repeat = input("정말로 삭제하시겠습니까?\n삭제를 원하시면 '네' 를 입력하세요.")
                if repeat == "네":           # 삭제 확인
                    print("삭제되었습니다.")
                    del address_list[x]     # address_list에 해당 행을 삭제
                    d.close
                break
    elif user_serch_num == "3" or user_serch_num == "이메일":  # 이메일로 삭제할 경우
        user_serch = input("삭제할 데이터의 이메일을 입력하세요.\n-> ")
        for x in range(len(address_list)):  # 행 수
            c = address_list[x][2]          # [x행][2열 = email]
            if user_serch == c:         # 슬라이싱
                repeat = input("정말로 삭제하시겠습니까?\n삭제를 원하시면 '네' 를 입력하세요.")
                if repeat == "네":           # 삭제 확인
                    print("삭제되었습니다.")
                    del address_list[x]     # address_list에 해당 행을 삭제
                    d.close
                break
    else:                                   # 메뉴를 잘못 입력했을 경우
        print("메뉴에 해당되지 않습니다. 처음으로 돌아갑니다.")
        
    e = open('book.csv', 'w', newline='')   # 'w'로 쓰기함수 (쓰기함수 사용할 경우 csv파일 내용이 포맷되는 것을 이용)
    e_writer = csv.writer(e)
        
    for i in address_list:                  # address_list의 len은 행 수이므로 삭제되고 남은 행만큼 루프
        writer_list.append(i[0])            # name 부분
        writer_list.append(i[1])            # phone 부분
        writer_list.append(i[2])            # email 부분
        
        e_writer.writerow(writer_list)      # writerow로 행에 내용 추가
        writer_list.clear()                 # writer_list를 clear를 하여 초기화
        
    e.close

while True:                 # main
    print("*" * 40)
    user_in = input("(메뉴)\n\n\t1.전체조회 -> 1\n\t2.부분조회 -> 2\n\t3.추가 -> 3\n\t4.삭제 -> 4\n\n입력란 : ")  # 메뉴 구성
    
    if user_in == "1" or user_in == "전체조회":   # 전체 조회
        all_lookup()
    elif user_in == "2" or user_in == "부분조회":  # 부분 조회
        part_lookup()
    elif user_in == "3" or user_in == "추가":    # 추가
        add_data()
    elif user_in == "4" or user_in == "삭제":    # 삭제
        delete_data()
    elif user_in == "":     # 엔터 시
        break
    else:                   # 해당되는 메뉴가 없을 시
        print("메뉴에 해당하지 않는 내용입니다.")