N = int(input())
score = map(int, (input().split()))
score_list = list(score)

sum = 0
for num in score_list:
    sum += num/max(score_list)*100

average = sum/len(score_list)
print(average)
