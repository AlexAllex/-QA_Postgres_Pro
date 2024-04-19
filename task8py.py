import psycopg2
from faker import Faker
from random import randint, choice
from datetime import date

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="academy",
    user="user_name",
    password="password",
    host="my_host",
    port="my_port"
)

# Создание курсора для выполнения SQL-запросов
cur = conn.cursor()

# Инициализация генератора случайных данных
fake = Faker()

# Функция для генерации случайных данных и заполнения таблицы students
def populate_students(num_students):
    for _ in range(num_students):
        name = fake.name()
        start_year = fake.date_between(start_date='-4y', end_date='today')
        cur.execute("INSERT INTO students (name, start_year) VALUES (%s, %s)", (name, start_year))

# Функция для генерации случайных данных и заполнения таблицы courses
def populate_courses(num_courses):
    for _ in range(num_courses):
        title = fake.job()
        hours = round(randint(10, 100) + randint(0, 9) / 10, 1)
        cur.execute("INSERT INTO courses (title, hours) VALUES (%s, %s)", (title, hours))

# Функция для генерации случайных данных и заполнения таблицы exams
def populate_exams(num_exams):
    cur.execute("SELECT s_id FROM students")
    student_ids = [row[0] for row in cur.fetchall()]

    cur.execute("SELECT c_no FROM courses")
    course_ids = [row[0] for row in cur.fetchall()]

    for _ in range(num_exams):
        s_id = choice(student_ids)
        c_no = choice(course_ids)
        score = randint(0, 100)
        cur.execute("INSERT INTO exams (s_id, c_no, score) VALUES (%s, %s, %s)", (s_id, c_no, score))

# Вызов функций для заполнения таблиц данными
populate_students(50)  # Заполнение таблицы students 50 записями
populate_courses(10)   # Заполнение таблицы courses 10 записями
populate_exams(200)    # Заполнение таблицы exams 200 записями

# Подтверждение выполнения транзакции и закрытие соединения
conn.commit()
conn.close()
