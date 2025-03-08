from faker import Faker
from random import randint, choice
from sqlalchemy.orm import sessionmaker
from models import engine, Student, Group, Teacher, Subject, Grade
from datetime import datetime, timedelta

fake = Faker()
Session = sessionmaker(bind=engine)
session = Session()

# Створення груп
groups = [Group(name=f"Group-{i+1}") for i in range(3)]
session.add_all(groups)
session.commit()

# Створення викладачів
teachers = [Teacher(name=fake.name()) for _ in range(5)]
session.add_all(teachers)
session.commit()

# Створення предметів
subjects = [Subject(name=fake.word().capitalize(), teacher=choice(teachers)) for _ in range(8)]
session.add_all(subjects)
session.commit()

# Створення студентів
students = [Student(name=fake.name(), group=choice(groups)) for _ in range(50)]
session.add_all(students)
session.commit()

# Створення оцінок
for student in students:
    for subject in subjects:
        for _ in range(randint(5, 20)):
            grade = Grade(
                student=student,
                subject=subject,
                grade=randint(1, 10),
                date_received=fake.date_time_between(start_date="-1y", end_date="now")
            )
            session.add(grade)

session.commit()
session.close()

print("Database seeded successfully!")