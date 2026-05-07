"""
문제: 빈칸 채우기 - 가습기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/250127

가습기 모드(auto/target/minimum)와 습도, 설정값에 따라 작동 단계 반환.
주어진 4개 함수 중 적절한 것을 빈칸에 매칭.
"""


def func1(humidity, val_set):
    if humidity < val_set:
        return 3
    return 1


def func2(humidity):
    if humidity >= 50:
        return 0
    elif humidity >= 40:
        return 1
    elif humidity >= 30:
        return 2
    elif humidity >= 20:
        return 3
    elif humidity >= 10:
        return 4
    else:
        return 5


def func3(humidity, val_set):
    if humidity < val_set:
        return 1
    return 0


def solution(mode_type, humidity, val_set):
    answer = 0
    if mode_type == "auto":
        answer = func2(humidity)
    elif mode_type == "target":
        answer = func1(humidity, val_set)
    elif mode_type == "minimum":
        answer = func3(humidity, val_set)
    return answer