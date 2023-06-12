S = input()
S_list = list(S)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    if i in S_list:
        print(S_list.index(i), end=" ")
    else:
        print(-1, end=" ")
