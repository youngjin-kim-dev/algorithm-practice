-- 문제: 오프라인/온라인 판매 데이터 통합하기
-- 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131537

SELECT A.REST_ID, 
       A.REST_NAME, 
       A.FOOD_TYPE, 
       A.FAVORITES, 
       A.ADDRESS, 
       ROUND(AVG(B.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO A
JOIN REST_REVIEW B ON A.REST_ID = B.REST_ID
WHERE A.ADDRESS LIKE '서울%'
GROUP BY A.REST_ID
ORDER BY AVG(B.REVIEW_SCORE) DESC, A.FAVORITES DESC;