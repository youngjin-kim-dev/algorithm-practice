"""
문제: 빈칸 채우기 - 심폐소생술
링크: https://school.programmers.co.kr/learn/courses/30/lessons/340203

무작위 순서로 담긴 심폐소생술 단계 리스트 cpr이 주어질 때,
각 단계가 정상 순서에서 몇 번째인지 순서대로 반환.
"""


def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    
    for action in cpr:
        for i in range(len(basic_order)):
            if action == basic_order[i]:
                answer.append(i + 1)
    return answer