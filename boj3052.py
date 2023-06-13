left_list = []

for i in range(10):
    num = int(input())
    left = num%42
    left_list.append(left)

left_list = set(left_list)

print(len(left_list))