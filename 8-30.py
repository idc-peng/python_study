# 8주차 마지막 성적계산기

# Five Grades for the Grade Calculator program in action 
#   - dictionary 형태

jack = { "name":"Jack Frost", 
         "assignment" : [80, 50, 40, 20], 
         "test" : [75, 75], 
         "lab" : [78.20, 77.20] 
       }  
james = { "name":"James Potter", 
          "assignment" : [82, 56, 44, 30], 
          "test" : [80, 80], 
          "lab" : [67.90, 78.72] 
        } 
dylan = { "name" : "Dylan Rhodes", 
          "assignment" : [77, 82, 23, 39], 
          "test" : [78, 77], 
          "lab" : [80, 80] 
        } 
jess = { "name" : "Jessica Stone", 
         "assignment" : [67, 55, 77, 21], 
         "test" : [40, 50], 
         "lab" : [69, 44.56] 
       } 
tom = { "name" : "Tom Hanks", 
        "assignment" : [29, 89, 60, 56], 
        "test" : [65, 56], 
        "lab" : [50, 40.6] 
      }

dic = {}                # 각각의 학생들의 딕셔너리를 가져왔습니다.
x = 0                   # 네임을 한명씩 옮기기 위해 사용한 변수
name = [jack, james, dylan, jess, tom]  # 학생들의 이름 딕셔너리를 리스트로 만든것
total_score = 0         # 학급 전체 점수 합산

for i in name:
    print(i['name'])    # 학생의 이름 호출
    print('-' * 20)     # 구분선
    score = 0           # 학생별 평균
    avg_ass = 0         # 평균 assigmnet
    avg_test = 0        # 평균 test
    avg_lab = 0         # 평균 lab
    dic = name[x]
    avg_ass = (sum(dic['assignment']) / 4) * 0.1
    avg_test = (sum(dic['test']) / 2) * 0.7
    avg_lab = (sum(dic['lab']) / 2) * 0.2
    
    score = avg_ass + avg_test + avg_lab
    print('평균성적: %0.2f' % score)
    
    total_score += score
    
    if score >= 90:     # 학점을 나타내기 위해 사용한 if문
        print('평   점: A')
    elif score >= 80:
        print('평   점: B')
    elif score >= 70:
        print('평   점: C')
    elif score >= 60:
        print('평   점: D')
    else:
        print('평   점: F')
    
    print()
    x+=1                # 루프 한번을 할때마다 학생이 바껴야 되므로 증감한 값.

avg_total = total_score / 5 # 전체 학생의 평균

print('학급 평균: %0.2f' % avg_total)

if avg_total >= 90:     # 학급 평점 판별을 위한 if문
    print('학급 평점: A')
elif avg_total >= 80:
    print('학급 평점: B')
elif avg_total >= 70:
    print('학급 평점: C')
elif avg_total >= 60:
    print('학급 평점: D')
else:
    print('학급 평점: F')