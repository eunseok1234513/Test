n = int(input())
num = input()
num_list = list(num)

total = 0

for i in range(n):
    total += int(num_list[i])

print(total)
