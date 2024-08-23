-- 코드를 작성해주세요
SELECT ID, 
    CASE WHEN RANKS <=((SELECT COUNT(*) FROM ECOLI_DATA)*0.25) THEN 'CRITICAL'
         WHEN RANKS <=((SELECT COUNT(*) FROM ECOLI_DATA)*0.50) THEN 'HIGH'
         WHEN RANKS <=((SELECT COUNT(*) FROM ECOLI_DATA)*0.75) THEN 'MEDIUM'
         ELSE 'LOW'
    END AS COLONY_NAME
    FROM (
        SELECT ID, RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS RANKS
            FROM ECOLI_DATA
    ) AS A
ORDER BY 1;