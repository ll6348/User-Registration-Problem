import re
class UserRegistrationProblem:

    def check_first_name(self):
        is_true = True
        while is_true:
            self.first_name = input("Please enter your first name: ")
            if re.search('^[A-Z][a-zA-Z]{2,}$', self.first_name):
                print("Name is accepted")
                is_true = False
            else:
                print("Name shouch contain only alphabets and atleast 3 characters")

user_obj = UserRegistrationProblem()
user_obj.check_first_name()

