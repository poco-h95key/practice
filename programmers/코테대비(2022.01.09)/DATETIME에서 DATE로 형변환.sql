SELECT ANIMAL_ID, NAME
, REGEXP_REPLACE(TO_CHAR(DATETIME,'YYYYMMDD'), '(.{4})(.+)(.{2})', '\1-\2-\3') AS "날짜"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
