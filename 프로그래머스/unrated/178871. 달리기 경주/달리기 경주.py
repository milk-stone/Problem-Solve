def solution(players, callings):
    size = len(players)
    d1 = dict()
    d2 = dict()
    for i in range(size):
        d1[players[i]] = i
        d2[i] = players[i]
    for str1 in callings:
        num1 = d1[str1]
        num2 = num1 - 1
        str2 = d2[num2]
        d1[str1], d1[str2] = d1[str2], d1[str1]
        d2[num1], d2[num2] = d2[num2], d2[num1]
    answer = ['' for _ in range(size)]
    for str3 in players:
        answer[d1[str3]] = str3
    return answer