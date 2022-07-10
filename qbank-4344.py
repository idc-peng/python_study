user_in = int(input())

score_list = []
jug_list = []
percent_list = []

for i in range(user_in):
    score_list = list(map(int, input().split()))
    del score_list[0]
    avg = (sum(score_list)) / (len(score_list))
    for j in score_list:
        if j > avg:
            jug_list.append(j)
    percent_list.append((len(jug_list) / len(score_list)))
    score_list.clear()
    jug_list.clear()

for x in percent_list:
    print("%.3f%%" % (x * 100))

# 평균은 넘겠지
