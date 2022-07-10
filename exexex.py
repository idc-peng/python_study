# exexex 파일은 테스트용 파일임 python shell보다 편함

import csv

def all_lookup():                                       # 전체 조회 함수
    f = open('book_ex.csv', 'r', encoding='utf-8-sig')  # "r"로 읽기
    f_reader = csv.DictReader(f)
    address_list = {}                                   # 주소 담는 리스트
    count = 0
    
    for i in f_reader:                                  # csv 내용 address_list 에 저장
        for k, v in i.items():
            address_list[k] = v
            print(address_list[k])
    print
    
    print("     이름\t전화번호     이메일")                    # ui 구성용
        
    for x in range(len(address_list)):                  # len = csv파일 행 수
        if address_list == "":                          # 공란일 경우
                break
        else:                                           # name= 을 슬라이싱
            print("%-12s" % address_list, end = "")     # 글자 왼쪽 정렬
               
        if x % 3 == 2:
            print("\n")
            print("-" * 40)
        else:
            print(end = " /")
        count += 1
    print()
    
    f.close
    
while True:                                      # main
    print("*" * 40)
    user_in = input("(메뉴)\n\n\t1.전체조회 -> 1\n\t2.부분조회 -> 2\n\t3.추가 -> 3\n\t4.삭제 -> 4\n\n입력란 : ")  # 메뉴 구성
    
    if user_in == "1" or user_in == "전체조회":     # 전체 조회
        all_lookup()
    elif user_in == "2" or user_in == "부분조회":   # 부분 조회
        part_lookup()
    elif user_in == "3" or user_in == "추가":      # 추가
        add_data()
    elif user_in == "4" or user_in == "삭제":      # 삭제
        delete_data()
    elif user_in == "":                          # 엔터 시
        break
    else:                                        # 해당되는 메뉴가 없을 시
        print("메뉴에 해당하지 않는 내용입니다.")