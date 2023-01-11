from numpy import mean

all_students = []
all_lectures = []

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Student(Person):

    def __init__(self, name, surname, gender):
        super().__init__(name, surname)
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        all_students.append(self)


    def get_average_grade(self):
        average_grade_per_course = str()
        for key, value in self.grades.items():
           average_grade_per_course += f'Средняя оценка по предмету {key}: {mean(value)}\n'
        return average_grade_per_course

    def __str__(self):
        courses = ''
        finished_courses = ''
        for i in self.courses_in_progress:
            courses += f'{i} '
        for i in self.finished_courses:
            finished_courses += f'{i} '
        return f'\nИмя: {self.name} \nФамилия: {self.surname}\n{self.get_average_grade()}Курсы в процессе изучения: {courses}\n' \
               f'Завершенные курсы: {finished_courses if False else "Еще не закончил, но все впереди"}\n'

    def rate_mentor(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        all_lectures.append(self)
    def get_average_grade(self):
        average_grades = ''
        for key, value in self.grades.items():
            average_grades += f'Средняя оценка по предмету {key}: {mean(value)}\n'
        return average_grades



    def __str__(self):
        return f'\nИмя: {self.name} \nФамилия: {self.surname}\n{self.get_average_grade()}'



class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


#Тесты
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']

not_best_student = Student('Tim', 'Prokhorov', 'male')
not_best_student.courses_in_progress += ['GIT']


cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'GIT', 10)
cool_reviewer.rate_hw(not_best_student, 'Python', 8)
cool_reviewer.rate_hw(not_best_student, 'GIT', 10)

second_cool_reviewer = Reviewer('Buddy', 'Some')
second_cool_reviewer.courses_attached += ['Python']
second_cool_reviewer.rate_hw(best_student, 'Python', 7)
second_cool_reviewer.rate_hw(best_student, 'GIT', 10)
second_cool_reviewer.rate_hw(not_best_student, 'Python', 4)
second_cool_reviewer.rate_hw(not_best_student, 'GIT', 10)


cool_lecturer = Lecturer('Mike', 'Davidson')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']

second_cool_lecturer = Lecturer('Luca', 'Stricagnoli')
second_cool_lecturer.courses_attached += ['Python']


not_best_student.rate_mentor(cool_lecturer, 'GIT', 3)
not_best_student.rate_mentor(cool_lecturer, 'GIT', 4)
not_best_student.rate_mentor(second_cool_lecturer, 'GIT', 5)
not_best_student.rate_mentor(second_cool_lecturer, 'Python', 4)

best_student.rate_mentor(cool_lecturer, 'Python', 10)
best_student.rate_mentor(cool_lecturer, 'Python', 9)
best_student.rate_mentor(cool_lecturer, 'Python', 2)
best_student.rate_mentor(second_cool_lecturer, 'Python', 10)
best_student.rate_mentor(second_cool_lecturer, 'Git', 9)
best_student.rate_mentor(second_cool_lecturer, 'Python', 2)


def get_all_studs_grades(students, course='Python'):
    res = []
    for student in students:
        if course in student.grades.keys():
            for i in student.grades.values():
                res += i
            return f'Средняя отметка всех студентов по предмету {course}: {mean(res)}'
    else:
        return 'Еще никто не закончил'


def get_all_lectures_grades(lectures, course='Python'):
    res = []
    for lectur in lectures:
        if course in lectur.grades.keys():
            for i in lectur.grades.values():
                res += i
            return f'Средняя отметка всех лекторов по предмету {course}: {mean(res)}'
        else:
            return 'Оценок еще нет'




