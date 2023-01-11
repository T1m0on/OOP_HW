from numpy import mean

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
        return f'Имя: {self.name} \nФамилия: {self.surname}\n{self.get_average_grade()}Курсы в процессе изучения: {courses}\n' \
               f'Завершенные курсы: {finished_courses if False else "Еще не закончил, но все впереди"}'

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

    def get_average_grade(self):
        average_grade_per_course = str()
        for key, value in self.grades.items():
           average_grade_per_course += f'Средняя оценка по предмету {key}: {mean(value)}\n'
        return average_grade_per_course


    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}\n{self.get_average_grade()}'


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

cool_reviewer = Reviewer('Some', 'Buddy')

cool_lecturer = Lecturer('Mike', 'Davidson')

cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'GIT', 10)
cool_reviewer.rate_hw(best_student, 'Python', 2)
cool_reviewer.rate_hw(best_student, 'GIT', 1)
cool_reviewer.rate_hw(best_student, 'Python', 4)
cool_reviewer.rate_hw(best_student, 'GIT', 5)


cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['GIT']


not_best_student.courses_in_progress += ['GIT']
not_best_student.rate_mentor(cool_lecturer, 'GIT', 3)
not_best_student.rate_mentor(cool_lecturer, 'GIT', 4)

best_student.rate_mentor(cool_lecturer, 'Python', 10)
best_student.rate_mentor(cool_lecturer, 'Python', 9)
best_student.rate_mentor(cool_lecturer, 'Python', 2)

print(best_student)
print()
print(cool_reviewer)
print()
print(cool_lecturer)


