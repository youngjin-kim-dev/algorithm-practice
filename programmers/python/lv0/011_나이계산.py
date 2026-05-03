"""
문제: 빈칸 채우기 - 나이 계산
링크: https://school.programmers.co.kr/learn/courses/30/lessons/250131

출생 연도와 나이 종류(Korea/Year)가 주어질 때, 2030년 기준 나이 출력.
- 한국식: 2030 - year + 1
- 연 나이: 2030 - year
"""

year = int(input())
age_type = input()

if age_type == "Korea":
    answer = 2030 - year + 1
elif age_type == "Year":
    answer = 2030 - year

print(answer)