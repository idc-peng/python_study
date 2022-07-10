v=1
n=int(input("마방진의 행과 열을 무엇으로 할지 입력하시오(3이상 홀수);"))

pp = [ [0 for _ in range(n)]  for _ in range(n)   ]

h=(n+1)//2
k=1
###  print (k,"(",v,",",h,")")
pp[v-1][h-1] = k

while k<n*n:
    k+=1
    if(k%n==1):
        h-=1
    else:
        v-=1
        h-=1
        if(v<1):
            v=n
        if(h<1):
            h=n
    # print (k,"(",v,",",h,")")
    pp[v-1][h-1] = k

for m in range(n) :
    print(pp[m])