# 파이썬 새로운 내장함수 enumerate

solar1 = ["태양", "수", "금", "지", "화", "목", "토", "천", "해"]
solar2 = ['sun', 'Mecury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
exex_dict = {}

for i, k in enumerate(solar1):  # 이 뜻을 분석해보자.
    val = solar2[i]
    exex_dict[k] = val
                # 이 방식은 즉 enumerate을 사용하면 ex) 0 , 태양 / 1, 수 / 이런 식으로 나오는데 i = range와 비슷, k는 key값이 될 내용임을 이용
print(exex_dict)