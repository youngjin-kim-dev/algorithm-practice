"""
문제: 문자열 출력하기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181952?language=python3

정수 a와 b를 입력받아 'a = N', 'b = N' 형식으로 두 줄 출력.

입력: 4 5
출력:
a = 4
b = 5
"""

a, b = map(int, input().strip().split(' '))

print(f'a = {a}')
print(f'b = {b}')