import re
class UserRegistrationProblem:
    def __init__(self,name):
        self.name = name
    def check_name(self):
        is_true = True
        while is_true:
            self.name = input("Please enter your first name: ")
            if re.search('[a-zA-Z]{3,}', self.name):
                print("Name is accepted")
                is_true = False
            else:
                print("Name shouch contain only alphabets and atleast 3 characters")

name = input("Please enter your first name(Must only contain alphabets and atleast 3 characters): ")
user_obj = UserRegistrationProblem(name)
user_obj.check_name()

