CREATE TABLE students(s_id SERIAL PRIMARY KEY,
                       name VARCHAR(50),
                       start_year DATE);
                       
CREATE TABLE courses(c_no SERIAL PRIMARY KEY, 
                     title VARCHAR(50),
                     hours DECIMAL(4, 1)
                    );

                   
 CREATE TABLE exams(
                   s_id INT,
                   c_no INT ,
                   score INT,
                   FOREIGN KEY (s_id)  REFERENCES students (s_id), 
                   FOREIGN KEY (c_no)  REFERENCES courses (c_no)
                   );                  