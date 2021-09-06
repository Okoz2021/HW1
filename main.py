class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_grade(self):
        stud_list = []
        for grade in self.grades.values():
            for mark in grade:
                stud_list.append(mark)
        avg = sum(stud_list) / len(stud_list)
        return avg

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('None')
            return
        return self.avg_grade() < other.avg_grade()

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avg_grade()} \nКурсы в процессе изучения: {",".join(self.courses_in_progress)} \nЗавершенные курсы: {",".join(self.finished_courses)}\n '
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_in_progress = []
        self.grades = {}

    def lec_avg_grade(self):
        Lect_list = []
        for grade in self.grades.values():
            for mark in grade:
                Lect_list.append(mark)
        lec_avg = sum(Lect_list) / len(Lect_list)
        return round(lec_avg, 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('None')
            return
        return self.lec_avg_grade() < other.lec_avg_grade()

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.lec_avg_grade()}\n'
        return res


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
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['GIT']
best_student.finished_courses += ['Введение в программирование']

one_student = Student('John', 'One', 'gender')
one_student.courses_in_progress += ['Python']
one_student.courses_in_progress += ['Git']
one_student.finished_courses += ['Введение в программирование']

second_student = Student('Mary', 'Second', 'gender')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Введение в программирование']

students = [best_student, one_student, second_student]

# best_lecturer = Lecturer('Some', 'Buddy')

some_lecturer = Lecturer('SomeL', 'BuddyL')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

one_lecturer = Lecturer('OneL', 'AA')
one_lecturer.courses_attached += ['Python']
one_lecturer.courses_attached += ['Git']

second_lecturer = Lecturer('SecondL', 'BB')
second_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['Git']

lecturers = [some_lecturer, one_lecturer, second_lecturer]

some_reviewer = Reviewer('SomeR', 'BuddyR')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']

one_reviewer = Reviewer('OneR', 'A')
one_reviewer.courses_attached += ['Python']
one_reviewer.courses_attached += ['Git']

second_reviewer = Reviewer('SecondR', 'B')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['Git']

reviewer = [some_reviewer, one_reviewer, second_reviewer]

some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Git', 10)

some_reviewer.rate_hw(one_student, 'Python', 7)
some_reviewer.rate_hw(one_student, 'Python', 7)
some_reviewer.rate_hw(one_student, 'Python', 8)
some_reviewer.rate_hw(one_student, 'Git', 6)

some_reviewer.rate_hw(second_student, 'Python', 3)
some_reviewer.rate_hw(second_student, 'Python', 4)
some_reviewer.rate_hw(second_student, 'Python', 5)
some_reviewer.rate_hw(second_student, 'Git', 4)

best_student.rate_lectures(some_lecturer, 'Python', 10)
best_student.rate_lectures(some_lecturer, 'Python', 10)
best_student.rate_lectures(some_lecturer, 'Python', 10)
best_student.rate_lectures(some_lecturer, 'Python', 10)
best_student.rate_lectures(some_lecturer, 'Git', 10)

best_student.rate_lectures(one_lecturer, 'Python', 9)
best_student.rate_lectures(one_lecturer, 'Python', 8)
best_student.rate_lectures(one_lecturer, 'Python', 7)
best_student.rate_lectures(one_lecturer, 'Python', 9)
best_student.rate_lectures(one_lecturer, 'Git', 6)

best_student.rate_lectures(second_lecturer, 'Python', 10)
best_student.rate_lectures(second_lecturer, 'Python', 8)
best_student.rate_lectures(second_lecturer, 'Python', 7)
best_student.rate_lectures(second_lecturer, 'Python', 9)
best_student.rate_lectures(second_lecturer, 'Git', 6)

one_student.rate_lectures(some_lecturer, 'Python', 10)
one_student.rate_lectures(some_lecturer, 'Python', 10)
one_student.rate_lectures(some_lecturer, 'Python', 10)
one_student.rate_lectures(some_lecturer, 'Python', 10)
one_student.rate_lectures(some_lecturer, 'Git', 10)

one_student.rate_lectures(one_lecturer, 'Python', 9)
one_student.rate_lectures(one_lecturer, 'Python', 8)
one_student.rate_lectures(one_lecturer, 'Python', 7)
one_student.rate_lectures(one_lecturer, 'Python', 9)
one_student.rate_lectures(one_lecturer, 'Git', 7)

one_student.rate_lectures(second_lecturer, 'Python', 10)
one_student.rate_lectures(second_lecturer, 'Python', 8)
one_student.rate_lectures(second_lecturer, 'Python', 7)
one_student.rate_lectures(second_lecturer, 'Python', 9)
one_student.rate_lectures(second_lecturer, 'Git', 7)

second_student.rate_lectures(some_lecturer, 'Python', 10)
second_student.rate_lectures(some_lecturer, 'Python', 10)
second_student.rate_lectures(some_lecturer, 'Python', 10)
second_student.rate_lectures(some_lecturer, 'Python', 10)
second_student.rate_lectures(some_lecturer, 'Git', 10)

second_student.rate_lectures(one_lecturer, 'Python', 9)
second_student.rate_lectures(one_lecturer, 'Python', 8)
second_student.rate_lectures(one_lecturer, 'Python', 7)
second_student.rate_lectures(one_lecturer, 'Python', 9)
second_student.rate_lectures(one_lecturer, 'Git', 8)

second_student.rate_lectures(second_lecturer, 'Python', 10)
second_student.rate_lectures(second_lecturer, 'Python', 8)
second_student.rate_lectures(second_lecturer, 'Python', 7)
second_student.rate_lectures(second_lecturer, 'Python', 9)
second_student.rate_lectures(second_lecturer, 'Git', 9)

print('Students:')
print(best_student)
print(one_student)
print(second_student)

print()
print('Lecturers:')
print(some_lecturer)
print(one_lecturer)
print(second_lecturer)

print()
print('Reviewers:')
print(some_reviewer)
print(one_reviewer)
print(second_reviewer)
print()


# print(best_student.grades)
# print(some_lecturer.grades)
# print()


def avg_grade_kurs(students, course):
    mylist = []
    for student in students:
        if student.grades.get(course) != None:
            for kurs in student.grades.get(course):
                mylist.append(kurs)
        else:
            pass
    avg_grade_kurs = sum(mylist) / len(mylist)
    return avg_grade_kurs


avg_grade_kurs = avg_grade_kurs(students, course='Git')
print(f'Средняя оценка по домашнему заданию по всем студентам курса "Git" = {avg_grade_kurs}')
print()


def lec_avg_grade_kurs(lecturers, course):
    mylist = []
    for lecturer in lecturers:
        if lecturer.grades.get(course) != None:
            for kurs in lecturer.grades.get(course):
                mylist.append(kurs)
        else:
            pass
        lec_avg_grade_kurs = sum(mylist) / len(mylist)
    return lec_avg_grade_kurs


lec_avg_grade_kurs = lec_avg_grade_kurs(lecturers, course='Git')
print(f'Средняя оценка за лекции всех лекторов в рамках курса "Git" = {lec_avg_grade_kurs}')