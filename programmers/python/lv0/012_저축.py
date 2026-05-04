"""
문제: 빈칸 채우기 - 저축
링크: https://school.programmers.co.kr/learn/courses/30/lessons/250130

100만 원 모으는데 걸리는 개월 수 출력.
- 70만 원까지는 매월 before씩 저축
- 70만 원 이후는 매월 after씩 저축
"""

start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    month += 1
while money < 100:
    money += after
    month += 1

print(month)