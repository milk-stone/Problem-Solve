-- 코드를 작성해주세요
SELECT distinct d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
FROM SKILLCODES as s, DEVELOPERS as d
WHERE (s.NAME = "Python" or s.NAME = "C#") and s.CODE & d.SKILL_CODE
ORDER BY d.ID ASC;