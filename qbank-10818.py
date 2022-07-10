loop = int(input())

num_list = list(map(int,input().split()))

if len(num_list) == loop:
    print("%d %d" % (min(num_list), max(num_list)))
else:
    pass

# 최소, 최대
