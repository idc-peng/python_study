def hansu(num):
    result = 0
    if num <= 99:
        for i in range(num):
            result += 1
    else:
        result += 99
        for x in range(100, num+1):
            num_str = str(x)
            if (int(num_str[0]) - int(num_str[1])) == (int(num_str[1]) - int(num_str[2])):
                result += 1
    return result


user_in = int(input())
nums = hansu(user_in)

print(nums)

# 한수
