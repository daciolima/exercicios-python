from operator import itemgetter


class School:
    def __init__(self):
        self.students = []

    # Add alunos na lista
    def add_student(self, name, grade):
        self.students.append([name, grade])

    # Retorna lista atraves do itemgetther pela grade e depois por nome. Conforme index.
    # Ondena os alunos pela grade e dentro de cada grade ordena os nomes.
    def roster(self):
        return [name[0] for name in sorted(self.students, key=itemgetter(1, 0))]

    def grade(self, grade_number):
        return sorted([student[0] for student in self.students if student[1] == grade_number])


# Using lambda
# class School:
#     def __init__(self):
#         self.students = []
#
#     def add_student(self, name, grade):
#         self.students.append([name, grade])
#
#     def roster(self):
#         return [name[0] for name in sorted(self.students, key=lambda x: f"{x[1]}{x[0]}")]
#
#     def grade(self, grade_number):
#         return sorted([student[0] for student in self.students if student[1] == grade_number])
