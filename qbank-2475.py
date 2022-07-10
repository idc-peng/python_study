# 문제은행 2475 - 검증수

while True:
    lis = input("고유번호 5자리를 빈칸을 두고 입력하시오. ex)1 2 3 4 5\n입력 -> ").split()
    sums = 0
    
    for i in lis:
        sums += (int(i) * int(i))
    
    print("고유번호 끝자리는 %d 입니다." % (sums % 10))