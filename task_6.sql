SELECT students.s_id, name,COUNT(exams.c_no) AS Количество_сданных_экзаменов
FROM students JOIN exams ON students.s_id = exams.s_id
              JOIN courses ON courses.c_no = exams.c_no
WHERE  exams.score IS NOT NULL            
GROUP BY students.s_id 
 ORDER BY students.s_id;
