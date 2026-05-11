"""
문제: 문자열 반복해서 출력하기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/181950

문자열 str과 정수 n을 입력받아 str을 n번 이어 붙여 출력.

입력: string 5
출력: stringstringstringstringstring
"""

str, n = input().strip().split(' ')
n = int(n)

print(str * n)