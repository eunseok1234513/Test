num_list = []

for i in range(9):
    numbers = int(input())
    num_list.append(numbers)

print(max(num_list))
print(num_list.index(max(num_list)) + 1)
