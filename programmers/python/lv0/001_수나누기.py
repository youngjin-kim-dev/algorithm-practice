"""
문제: 디버깅 - 두 자리씩 잘라서 더하기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/340205

2자리 이상의 정수 number를 2자리씩 자른 뒤, 자른 수를 모두 더한 합 출력.
1줄만 수정해서 버그 고치기.
"""

number = int(input())

answer = 0

for i in range(len(str(number)) // 2):
    answer += number % 100
    number //= 100

print(answer)