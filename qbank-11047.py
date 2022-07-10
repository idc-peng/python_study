# 문제은행 11047 - 동전 최솟값 문제

while True:
    user_in = input("동전의 종류 수를 입력하세요!\n-> ").split()
    coin_list = []
    coin_count = []
    cash = int(user_in[1])
    
    for i in range(int(user_in[0])):
        a = int(input("동전을 입력하세요!\n-> "))
        coin_list.append(a)
        
    coin_list.sort()
    coin_list.reverse()
    
    for i in coin_list:
        coin_count.append((cash - (cash % i)) / i)
        cash = (cash % i)
        
        if cash == 0:
            break
            
    print("첫째 줄에 %d 원을 만드는데 필요한 동전 개수의 최솟값은 %d 입니다." % (int(user_in[1]), sum(coin_count)))