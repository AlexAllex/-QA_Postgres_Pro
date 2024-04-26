SELECT  title,  ROUND(AVG(score),2) AS Средний_балл
FROM courses JOIN exams ON courses.c_no= exams.c_no
GROUP BY title
ORDER BY Средний_балл DESC ;
