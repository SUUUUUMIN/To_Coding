-- 코드를 작성해주세요
SELECT F.ID
FROM ECOLI_DATA AS F
    JOIN ECOLI_DATA AS S ON F.PARENT_ID = S.ID
    JOIN ECOLI_DATA AS T ON S.PARENT_ID = T.ID
WHERE T.PARENT_ID IS NULL
ORDER BY F.ID;