"""
문제: 빈칸 채우기 - 버스
링크: https://school.programmers.co.kr/learn/courses/30/lessons/340201

영진이가 버스에 탄 순간 빈 좌석 수 반환.
주어진 4개 함수 중 적절한 것을 빈칸에 채워서 solution 완성.
"""


def func1(num):
    if 0 > num:
        return 0
    else:
        return num


def func2(num):
    if num > 0:
        return 0
    else:
        return num


def func3(station):
    num = 0
    for people in station:
        if people == "Off":
            num += 1
    return num


def func4(station):
    num = 0
    for people in station:
        if people == "On":
            num += 1
    return num


def solution(seat, passengers):
    num_passenger = 0
    for station in passengers:
        num_passenger += func4(station)
        num_passenger -= func3(station)
    answer = seat - func1(num_passenger)
    return answer