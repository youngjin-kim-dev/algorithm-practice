"""
문제: 디버깅 - 물 부족
링크: https://school.programmers.co.kr/learn/courses/30/lessons/340202

월별 물 사용량 변화율을 적용해서 몇 달 뒤 저수지 물이 부족해지는지 반환.
1줄만 수정해서 버그 고치기.
"""


def solution(storage, usage, change):
    total_usage = 0
    for i in range(len(change)):
        usage = int(usage * (1 + change[i]/100))
        total_usage += usage
        if total_usage > storage:
            return i
    
    return -1