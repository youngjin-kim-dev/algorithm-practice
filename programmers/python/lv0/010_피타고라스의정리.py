"""
문제: 디버깅 - 피타고라스의 정리
링크: https://school.programmers.co.kr/learn/courses/30/lessons/250132

직각삼각형의 한 변 a와 빗변 c가 주어질 때, 다른 한 변의 길이의 제곱(b_square) 출력.
1줄만 수정해서 버그 고치기.
"""

a = int(input())
c = int(input())

b_square = c**2 - a**2
print(b_square)