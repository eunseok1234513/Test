words = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]):     #j가 단어 길이보다 작으면 인덱스 범위 안에 있으므로 출력할 수 있다.
            print(words[i][j], end='')