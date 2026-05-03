"""
문제: 디버깅 - 닉네임 규칙
링크: https://school.programmers.co.kr/learn/courses/30/lessons/340200

사용할 수 없는 닉네임을 규칙에 따라 변환.
1줄만 수정해서 버그 고치기.
"""


def solution(nickname):
    answer = ""
    for letter in nickname:
        if letter == "l":
            answer += "I"
        elif letter == "w":
            answer += "vv"
        elif letter == "W":
            answer += "VV"
        elif letter == "O":
            answer += "0"
        else:
            answer += letter
    while len(answer) < 4:
        answer += "o"
    if len(answer) > 8:
        answer = answer[:8]
    return answer