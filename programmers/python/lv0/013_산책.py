"""
문제: 디버깅 - 가채점
링크: https://school.programmers.co.kr/learn/courses/30/lessons/250128

route(N/S/E/W로 구성된 문자열)에 따라 1m 단위로 이동.
출발점 기준 [동쪽 거리, 북쪽 거리] 형태로 최종 위치 반환.
"""


def solution(route):
    east = 0
    north = 0
    for i in route:
        if i == "N":
            north += 1
        elif i == "S":
            north -= 1
        elif i == "E":
            east += 1
        elif i == "W":
            east -= 1
    return [east, north]