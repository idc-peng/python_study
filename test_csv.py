import csv

f = open("매수종목.csv", 'w')
a = csv.writer(f)
a.writerow(['종목명', '종목코드', 'PER'])
a.writerow(['삼성전자', '005930', 15.79])
a.writerow(['NAVER', '035420', 55.82])
f.close()
