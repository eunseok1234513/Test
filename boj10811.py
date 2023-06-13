N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for k in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for h in range(N):
    print(basket[h], end=" ")