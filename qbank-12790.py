# 문제은행 12790 - 미니 판타지 워 (겜 이름)

while True:
    user_in = int(input("캐릭터의 수를 입력하세요~\n입력란 -> "))
    sta = []
    
    for i in range(user_in):
        hp, mp, atk, de, hp_, mp_, atk_, de_ = input("스탯을 입력하세요\n입력란 -> ").split()
        a_hp = int(hp) + int(hp_)
        a_mp = int(mp) + int(mp_)
        a_atk = int(atk) + int(atk_)
        a_de = int(de) + int(de_)
        
        if a_hp <= 0:
            a_hp = 1
        if a_mp <= 0:
            a_mp = 1
        if a_atk < 0:
            a_atk = 0
        sta.append(a_hp + (5*a_mp) + (a_atk*2) + (a_de*2))
        print()
    
    for i in sta:
        print(i)
    