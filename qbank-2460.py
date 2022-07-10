# 문제은행 2460 - 지능형 기차역

while True:
    aft_peo = 0
    people = []
    print("내린사람 / 탄사람")

    for i in range(10):
        a, b = input().split()
        
        aft_peo = aft_peo + int(b) - int(a)
        people.append(aft_peo)
    
    print("%d 명" % max(people))
    print("-" * 25)