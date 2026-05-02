"""
문제: 디버깅 - 병과분류
링크: https://school.programmers.co.kr/learn/courses/30/lessons/340204?language=python3

환자 코드의 마지막 4글자에 따라 병과를 출력.
빈칸 5곳을 채워서 코드 완성.
"""

code = input()
last_four_words = code[-4:]

if last_four_words == "_eye":
    print("Ophthalmologyc")
elif last_four_words == "head":
    print("Neurosurgery")
elif last_four_words == "infl":
    print("Orthopedics")
elif last_four_words == "skin":
    print("Dermatology")
else:
    print("direct recommendation")