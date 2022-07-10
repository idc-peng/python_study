while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# A+B - 4       아무 조건이 없으면 예외처리라도 해야한다
