"""
문제: 디버깅 - 가채점
링크: https://school.programmers.co.kr/learn/courses/30/lessons/250128

학생들이 가채점한 점수와 실제 성적이 같은지 비교.
1줄만 수정해서 버그 고치기.
"""


def solution(numbers, our_score, score_list):
    answer = []
    for i in range(len(numbers)):
        if our_score[i] == score_list[numbers[i] - 1]:
            answer.append("Same")
        else:
            answer.append("Different")
    return answer