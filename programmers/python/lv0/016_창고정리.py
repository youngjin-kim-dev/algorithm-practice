"""
문제: 디버깅 - 창고 정리
링크: https://school.programmers.co.kr/learn/courses/30/lessons/250126

같은 물건끼리 합쳐서 — 가장 개수가 많은 물건의 이름 반환.
1줄만 수정해서 버그 고치기.
"""


def solution(storage, num):
    clean_storage = []
    clean_num = []
    for i in range(len(storage)):
        if storage[i] in clean_storage:
            pos = clean_storage.index(storage[i])
            clean_num[pos] += num[i]
        else:
            clean_storage.append(storage[i])
            clean_num.append(num[i])
    
    max_num = max(clean_num)
    answer = clean_storag