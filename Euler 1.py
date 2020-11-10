num = 1
nums = []
while num < 1000:
    if num % 3 == 0 or num % 5 == 0:
        nums.append(num)
    num += 1
print(sum(nums))
