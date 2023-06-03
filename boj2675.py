n = int(input())

for _ in range(n):
    S, R = input().split()
    S = int(S)
    R_list = list(R)
    for i in range(len(R_list)):
        print(S*R_list[i], end="")
    print()
