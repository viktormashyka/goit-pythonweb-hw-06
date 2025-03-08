from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from models import engine, Student, Grade, Subject, Teacher, Group

Session = sessionmaker(bind=engine)
session = Session()

def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    result = session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))\
        .join(Grade)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc())\
        .limit(5)\
        .all()
    return result

def select_2(subject_id):
    """Знайти студента із найвищим середнім балом з певного предмета."""
    result = session.query(Student.name, func.avg(Grade.grade).label("avg_grade"))\
        .join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Student.id)\
        .order_by(func.avg(Grade.grade).desc())\
        .limit(1)\
        .all()
    return result

def select_3(subject_id):
    """Знайти середній бал у групах з певного предмета."""
    result = session.query(Group.name, func.avg(Grade.grade).label("avg_grade"))\
        .join(Student).join(Grade)\
        .filter(Grade.subject_id == subject_id)\
        .group_by(Group.id)\
        .all()
    return result

def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""
    result = session.query(func.avg(Grade.grade)).scalar()
    return result

def select_5(teacher_id):
    """Знайти які курси читає певний викладач."""
    result = session.query(Subject.name).filter(Subject.teacher_id == teacher_id).all()
    return result

def select_6(group_id):
    """Знайти список студентів у певній групі."""
    result = session.query(Student.name).filter(Student.group_id == group_id).all()
    return result

def select_7(group_id, subject_id):
    """Знайти оцінки студентів у окремій групі з певного предмета."""
    result = session.query(Student.name, Grade.grade)\
        .join(Grade)\
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)\
        .all()
    return result

def select_8(teacher_id):
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    result = session.query(func.avg(Grade.grade))\
        .join(Subject)\
        .filter(Subject.teacher_id == teacher_id)\
        .scalar()
    return result

def select_9(student_id):
    """Знайти список курсів, які відвідує певний студент."""
    result = session.query(Subject.name)\
        .join(Grade)\
        .filter(Grade.student_id == student_id)\
        .distinct()\
        .all()
    return result

def select_10(student_id, teacher_id):
    """Список курсів, які певному студенту читає певний викладач."""
    result = session.query(Subject.name)\
        .join(Grade)\
        .filter(Grade.student_id == student_id, Subject.teacher_id == teacher_id)\
        .distinct()\
        .all()
    return result
