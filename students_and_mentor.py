class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        grade_sum = 0
        grade_num = 0
        for grade_list in list(self.grades.values()):
            grade_sum += sum(grade_list)
            grade_num += len(grade_list)
        grade_stat = round(grade_sum/grade_num, 1)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {grade_stat}'
        return res

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached
            and course in student.courses_in_progress and 0 <= grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lecture_grade(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
            and course in self.courses_in_progress and 0 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        grade_sum = 0
        grade_num = 0
        for grade_list in list(self.grades.values()):
            grade_sum += sum(grade_list)
            grade_num += len(grade_list)
        if grade_num == 0:
            grade_stat = "Нет оценок"
        else:
            grade_stat = round(grade_sum/grade_num, 1)
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n\
            \rСредняя оценка за домашние задания: {grade_stat}\n\
            \rКурсы в процессе изучения: {" ".join(self.courses_in_progress)}\n\
            \rЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res
        
first_student = Student("Piter", "Ivanov", "man")
second_student = Student("Vova", "Petrov", "man")
first_student.courses_in_progress += ["Python"]
second_student.courses_in_progress += ["Java"]
first_student.finished_courses += ["Git"]

green_lector = Lecturer("Sidor", "Petrovich")
red_lector = Lecturer("Rinat", "Torvald")
green_lector.courses_attached += ["Python"]
red_lector.courses_attached += ["Java"]
green_lector.courses_attached += ["Git"]

old_reviwer = Reviewer("Varvara", "Reut")
new_reviwer = Reviewer("Tolik", "Chekushin")
old_reviwer.courses_attached += ["Python"]
new_reviwer.courses_attached += ["Java"]
old_reviwer.courses_attached += ["Git"]

first_student.lecture_grade(green_lector, "Python", 10)
print(green_lector.grades)

new_reviwer.rate_hw(second_student, "Java", 8)
old_reviwer.rate_hw(first_student, "Git", 7)
print(second_student.grades)
print(first_student.grades)

print(old_reviwer)
print(green_lector)
print(second_student)
print(first_student)