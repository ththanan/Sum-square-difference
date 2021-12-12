# Problem 6

nums = []
for i in range(1,101):
    a = i*i
    nums.append(a)
total = 0
for n in nums:
    total += n

sum = 0
for a in range(1,101):
    sum += a
answer = (sum*sum) - total
print(answer)