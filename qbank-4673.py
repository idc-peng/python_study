def self_number():
    # sets = set()
    # for i in range(1, 10000):
    #     if i < 10:
    #         x = i + i
    #     elif 10 <= i < 100:
    #         x = i + (i // 10) + (i % 10)
    #     elif 100 <= i < 1000:
    #         x = i + (i // 100) + ((i % 100) // 10) + (i % 10)
    #     elif 1000 <= i < 10000:
    #         x = i + (i // 1000) + ((i % 1000) // 100) \
    #             + ((i % 100) // 10) + (i % 10)
    #     sets.add(x)
    #
    # return sets
    sets = set()
    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        sets.add(i)

    return sets


nature_number_set = set(range(1, 10001))
self_number_set = self_number()

nums = nature_number_set - self_number_set
for x in sorted(nums):
    print(x)

# 셀프 넘버
