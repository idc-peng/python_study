# 문제은행 2587 - 대표값(평균과 중앙값)

while True:
    lis = []
    
    for i in range(5):
        a = int(input("수를 입력하세요\n입력 : "))
        lis.append(a)
    
    lis.sort()
    
    print("평균은 %d / 중앙값은 %d" % ((sum(lis)//len(lis)), lis[2]))