"""
2. Деканат.

Задание: спроектируйте следующую предметную область, используя объектно-ориентированный подход.

Сотрудники деканата каждый семестр решают проблему формирования отчетных ведомостей студентов, разных групп и курсов.
Цель - получить информацию о среднем балле каждого студента, группы, а также предмета(например, средний балл по
физкультуре в группе 433 составляет 4.1). Такая информация поможет сформировать список студентов, которых нужно
отчислить и стипендиатов, а также наиболее "проблемные" предметы.

"""


class Student:
    def __init__(self, name):

        self.name = name
        self.courses = []
        self.grades = []

    def calculate_average_score(self):
        total_score = sum(self.grades)
        average_score = total_score / len(self.grades)
        return average_score


class Group:
    def __init__(self, group_id):
        self.group_id = group_id
        self.students = []
        self.subjects = []

    def calculate_average_score(self):
        total_score = 0
        total_students = len(self.students)

        for subject in self.subjects:
            subject_total_score = 0
            for student in self.students:
                index = self.subjects.index(subject)
                subject_total_score += student.grades[index]
            subject_average_score = subject_total_score / total_students
            total_score += subject_average_score

        average_score = total_score / len(self.subjects)
        return average_score

    def calculate_average_score_by_subject(self, subject_name):
        subject_total_score = 0
        total_students = len(self.students)
        for student in self.students:
            index = student.subjects.index(subject_name)
            subject_total_score += student.grades[index]
        subject_average_score = subject_total_score / total_students
        print(f"Average score in {subject_name} in group {self.group_id}: {subject_average_score}")


class Subject:
    def __init__(self, subjects_id, subjects_name):
        self.subjects_id = subjects_id
        self.subjects_name = subjects_name
        self.students = []
        self.grades = []

    def calculate_average_score(self):
        total_score = sum(self.grades)
        average_score = total_score / len(self.grades)
        return average_score


class Deanery:
    def __init__(self):
        self.students = []
        self.groups = []
        self.subjects = []

    def calculate_average_score_by_group(self):
        for group in self.groups:
            average_score = group.calculate_average_score()
            print(f"Average score in {group.group_id}: {average_score}")

    def calculate_average_score_by_student(self):
        for student in self.students:
            average_score = student.calculate_average_score()
            print(f"Average score of {student.name} : {average_score}")


s1 = Student("Иванов Иван")
s1.subjects = ["Математика", "Физика", "ООП"]
s1.grades = [4, 4, 3]

s2 = Student("Сергеева Виктория")
s2.subjects = ["Математика", "Физика", "ООП"]
s2.grades = [5, 5, 4]

s3 = Student("Яковлев Олег")
s3.subjects = ["Математика", "Физика", "ООП"]
s3.grades = [5, 3, 4]

g1 = Group("430-1")
g1.students = [s1, s2]
g1.subjects = ["Математика", "Физика", "ООП"]

g2 = Group("430-2")
g2.students = [s3]
g2.subjects = ["Математика", "Физика", "ООП"]

c1 = Subject(1, "Математика")
c1.students = [s1, s2, s3]
c1.grades = [4.0, 3.5, 4.5]

c2 = Subject(2, "Физика")
c2.students = [s1, s2, s3]
c2.grades = [4.5, 4.0, 4.5]

c3 = Subject(3, "ООП")
c3.students = [s1, s2, s3]
c3.grades = [3.5, 4.0, 4.0]

staff = Deanery()
staff.students = [s1, s2, s3]
staff.groups = [g1, g2]
staff.subjects = [c1, c2, c3]


staff.calculate_average_score_by_group()

staff.calculate_average_score_by_student()

g1.calculate_average_score_by_subject("Математика")
g2.calculate_average_score_by_subject("Математика")






