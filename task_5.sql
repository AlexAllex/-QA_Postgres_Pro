SELECT students.s_id, name, score, COUNT(exams.c_no) AS SUMM
FROM  students JOIN exams ON students.s_id = exams.s_id
               JOIN courses ON courses.c_no = exams.c_no

WHERE score IS NULL 
GROUP BY students.s_id,name, score
HAVING COUNT(exams.c_no) = 4; 