-- 문제: 과일로 만든 아이스크림 고르기
-- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/133025

-- 풀이 1: JOIN 사용 (실무 표준)
SELECT A.FLAVOR
FROM FIRST_HALF A
JOIN ICECREAM_INFO B ON A.FLAVOR = B.FLAVOR
WHERE A.TOTAL_ORDER > 3000
  AND B.INGREDIENT_TYPE = 'fruit_based'
ORDER BY A.TOTAL_ORDER DESC;

-- 풀이 2: 서브쿼리 사용
-- SELECT FLAVOR
-- FROM FIRST_HALF
-- WHERE TOTAL_ORDER > 3000
--   AND FLAVOR IN (
--     SELECT FLAVOR
--     FROM ICECREAM_INFO
--     WHERE INGREDIENT_TYPE = 'fruit_based'
--   )
-- ORDER BY TOTAL_ORDER DESC;