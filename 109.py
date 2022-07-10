fruit = {"봄": "딸기", "여름" : "토마토", "가을" : "사과"}
print("제가좋아하는계절은: ", end=' ')
user = input()

if user in fruit :
    print("정답입니다.")
else :
    print("오답입니다.")
