
a = list(map(lambda x: (x // 10)*(x % 10), range(10, 100)))
count = 0

for i in a:
    print(i)
    count += 1
    if count == 10:
        print()
        print("*" * 10)
        count = 0

b = [i**2 for i in range(5) if i % 2 == 0]
print(b)


def test_packing(**pack):
    for key, value in pack.items():
        print("{} 이름은 {}입니다.".format(key, value))


test_packing(a='가가', b='나나')

cal = lambda a, b: a+b
print(cal(3, 4))


import time


def run_time_decorator(func_name):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func_name(*args, **kwargs)
        end_time = time.time()
        print('함수 실행 시간 : {}'.format(end_time - start_time))

        return result
    return wrapper


@run_time_decorator
def big_loop(num):
    data = list(range(1, num+1))
    result = []
    for x in data:
        temp = 0
        for y in range(1, x+1):
            temp += y ** 2
        result.append(temp)

    print("결과값은 {} 입니다.".format(sum(result)))
    return sum(result)


big_loop(1000)
