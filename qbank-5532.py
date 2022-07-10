# 문제은행 5532 - 방학숙제

while True:
    limit, mat, kor, kor_time, mat_time = input("얼마나 공부할 수 있나요?\n입력란 -> ").split()
    a = 0
    b = 0
       
    a = int(mat) // int(mat_time)
    b = int(kor) // int(kor_time)
    
    if a > b:
        c = int(limit) - a
        
        print("%d 일" % c)
    else:
        c = int(limit) - b
        
        print("%d 일" % c)