student = [i for i in range(1, 31)]

for h in range(28):
    num = int(input())
    student.remove(num)

print(min(student))
print(max(student))

