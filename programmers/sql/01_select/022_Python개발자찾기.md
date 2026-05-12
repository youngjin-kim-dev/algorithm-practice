# Python 개발자 찾기

[프로그래머스 문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/276013)

## 문제 요약
DEVELOPER_INFOS 테이블에서 — Python 스킬(SKILL_1, SKILL_2, SKILL_3 중 하나)을 
가진 개발자의 ID, EMAIL, FIRST_NAME, LAST_NAME 조회.
- ID 오름차순 정렬

## 풀이
\`\`\`sql
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPER_INFOS
WHERE 'Python' IN (SKILL_1, SKILL_2, SKILL_3)
ORDER BY ID;
\`\`\`

## 1차 시도 — `||` 연산자 (통과는 했으나 비표준)
\`\`\`sql
WHERE SKILL_1 = 'Python' || SKILL_2 = 'Python' || SKILL_3 = 'Python'
\`\`\`

**문제점**:
- `||`는 SQL 표준 아님
- MySQL은 OR로 작동, 다른 DB(Oracle, PostgreSQL)에선 문자열 연결
- 다른 DB에선 작동 안 함 → 이식성 나쁨

## 배운 점

### `||` 비표준 — `OR` 사용해야
| DB | `||`의 의미 |
|---|---|
| MySQL | OR (모드에 따라) |
| Oracle | 문자열 연결 |
| PostgreSQL | 문자열 연결 |
| SQL Server | 에러 |

**SQL 표준**: `OR` 사용. 어디서든 작동.

### `IN`의 좌우 반대 응용
이전 학습 — `IN (값1, 값2, 값3)`:
\`\`\`sql
WHERE 컬럼 IN (값1, 값2, 값3)
\`\`\`

이번 응용 — 값 하나가 여러 컬럼 중 하나와 일치:
\`\`\`sql
WHERE 값 IN (컬럼1, 컬럼2, 컬럼3)
\`\`\`

`IN`은 — 양쪽 바뀌어도 의미 같음. 활용 폭 넓음.

### 같은 값 여러 컬럼 비교 패턴
\`\`\`sql
-- 비추 (반복적)
WHERE SKILL_1 = 'Python' 
   OR SKILL_2 = 'Python' 
   OR SKILL_3 = 'Python'

-- 추천 (간결)
WHERE 'Python' IN (SKILL_1, SKILL_2, SKILL_3)
\`\`\`

같은 결과지만 — IN이 더 깔끔, 확장성 좋음.

## 다른 풀이 — OR 사용 (표준)
\`\`\`sql
WHERE SKILL_1 = 'Python' 
   OR SKILL_2 = 'Python' 
   OR SKILL_3 = 'Python'
\`\`\`

표준 SQL. IN과 결과 동일. 가독성은 IN이 우위.

## 메타 학습 — 통과 ≠ 표준
SQL 문제 — 통과했어도 표준 풀이가 다를 수 있음.
\`||` 같은 비표준 연산자 — 우연히 작동해도 다른 환경에서 깨질 가능성.

**원칙**: 표준 SQL 키워드 사용. 이식성 좋고 어디서든 작동.

## 데이터베이스 설계 관점 (참고)
이 문제 — SKILL_1, SKILL_2, SKILL_3로 컬럼 3개 분리.

실무에선 — 이게 **나쁜 설계** (1NF 위반).
더 좋은 설계:
- DEVELOPER 테이블 (ID, 이름 등)
- SKILL 테이블 (DEVELOPER_ID, SKILL_NAME) — 별도 테이블

그러면 — JOIN으로 처리:
\`\`\`sql
SELECT D.ID, D.EMAIL, ...
FROM DEVELOPER D
JOIN SKILL S ON D.ID = S.DEVELOPER_ID
WHERE S.SKILL_NAME = 'Python'
\`\`\`