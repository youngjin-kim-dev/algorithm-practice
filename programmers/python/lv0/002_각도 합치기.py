"""
문제: 디버깅 - 각도 합치기
링크: https://school.programmers.co.kr/learn/courses/30/lessons/340206

두 각의 합을 0도 이상 360도 미만으로 출력.
1줄만 수정해서 버그 고치기.
"""

angle1 = int(input())
angle2 = int(input())

sum_angle = angle1 + angle2
print(sum_angle % 360)