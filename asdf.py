
for i in range(1):
    m = open('book_ex.txt', 'r', encoding='utf-8')
    m_reader = f.readlines()
    
    for i in m_reader:
        for k, v in i.items():
            address_dict[person(k)] = v
            
    b = list(address_dict.values())
    
    print(b)
    
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