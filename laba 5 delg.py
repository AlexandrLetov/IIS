class Teacher:
    def __init__(self):
        self.Student = Student()

    def lesson(self):
        return 'Преподаватель читает лекцию'

    def clean_board(self):
        return self.Student.clean_board()


class Student:
    def clean_board(self):
        return 'Студент протёр доску'


parent = Teacher()
print(parent.lesson())
print(parent.clean_board())
