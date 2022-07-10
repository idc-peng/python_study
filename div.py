# 약수 구하기 2탄 메모장 이용하기

def div():
    f = open("C:/Users/cgj10/Desktop/py4e/in_data.txt", 'r')
    c = open("C:/Users/cgj10/Desktop/py4e/out_data.txt", 'w')
    while True:
        try:
            count = 0
            line = f.readline()
            a = int(line)
            print(a, "의 약수는 -> ", end = "")
            c.write("\n%d 의 약수는 -> " % a)
            for x in range(1, a+1):
                if a % x == 0:
                    if a == x :
                        print(x, end = " ")
                        c.write("%d" % x)
                        count += 1
                    else :
                        print(x, end = ", ")
                        c.write("%d, " % x)
                        count += 1
            print()
            print("약수의 개수는 -> %d 개" % count)
            c.write("\n약수의 개수는 -> %d 개\n" % count)
            c.write("-" * 25)
            print("-" * 40)
            f.close
        except ValueError:
            print("종료되었습니다.")
            break
    return count

print("메모장에 입력한 정수의 약수를 구하는 프로그램입니다.\n\n")
print("*" * 50)
div()