"""
문제: 덧셈식 출력하기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181947

두 정수 a, b를 입력받아 'a + b = c' 형식으로 출력.

입력: 4 5
출력: 4 + 5 = 9
"""

a, b = map(int, input().strip().split(' '))

print(f'{a} + {b} = {a + b}')