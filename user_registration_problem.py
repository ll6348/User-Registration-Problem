import re
class UserRegistrationProblem:

     def check_first_name(self):
        is_true = True
        while is_true:
            print("""Your first name should start with capital letter.
                  Should contain only alphabets.
                  Atleast must contain 3 characters.""")
            self.first_name = input("Please enter your first name: ")
            if re.fullmatch('^[A-Z][a-zA-Z]{2,}$', self.first_name):
                print("Name is accepted")
                is_true = False
            else:
                 print("Invalid Input.")

user_obj = UserRegistrationProblem()
user_obj.check_first_name()

