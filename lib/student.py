# lib/student.py

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, knowledge_string):
        # Add the provided string to the student's knowledge list
        self.knowledge.append(knowledge_string)
