A, B = input().split()
print("%.9f" % (int(A)/int(B)))

# 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.
# 이 말은 즉 소수점 9자리까진 출력해야 한다. %.9f = 소수점 9자리까지 출력
