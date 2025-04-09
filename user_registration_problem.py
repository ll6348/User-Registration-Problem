import re
class UserRegistrationProblem:

    def check_first_name(self):
        is_true = True
        while is_true:
            print("Your first name should Start with capital letter")
            print("Should contain only alphabets.")
            print("Atleast must contain 3 characters.")
            self.first_name = input("Please enter your first name: ")
            if re.fullmatch('^[A-Z][a-zA-Z]{2,}$', self.first_name):
                print("Name is accepted")
                is_true = False
            else:
                 print("Invalid Input.")
    
    def check_last_name(self):
        is_true = True
        while is_true:
            print("Your last name should Start with capital letter")
            print("Should contain only alphabets.")
            print("Atleast must contain 3 characters.")
            self.last_name = input("Please enter your last name: ")
            if re.fullmatch('^[A-Z][a-zA-Z]{2,}$', self.last_name):
                print("Name is accepted")
                is_true = False
            else:
                 print("Invalid Input.")

    def check_mail(self):
        is_true = True
        while is_true:
            print("E.g. abc.xyz@bl.co.in ")
            print("Email has 3 mandatory parts (abc, bl & co) and 2 optional (xyz & in) with precise @ and . positions")
            self.email = input("Please enter your email: ")
            if re.fullmatch(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.[a-zA-Z]{2,}){1,2}$', self.email):
                print("Email is accepted")
                is_true = False
            else:
                 print("Invalid Input.")

    def check_phone_number(self):
        is_true = True
        while is_true:
            print("E.g. 91 9919819801")
            print("Format : Country code followed by space and 10 digit number")
            self.phone_number = input("Please enter your phone number: ")
            if re.fullmatch(r'^\d{2}\s\d{10}$',  self.phone_number):
                print("Phone number is accepted")
                is_true = False
            else:
                 print("Invalid Input.")

    def check_password(self):
        is_true = True
        while is_true:
            print("As a User need to follow pre-defined Password rules.")
            print("Rule1 - minimum 8 Characters")
            self.password = input("Please enter your password: ")
            if re.fullmatch(r'^.{8,}$',  self.password):
                print("Password passed rule 1.")
                is_true = False
            if re.fullmatch(r'^.{1,7}$', self.password):
                 print("Password didn't pass the rule 1.")
                 continue

user_obj = UserRegistrationProblem()
user_obj.check_first_name()
user_obj.check_last_name()
user_obj.check_mail()
user_obj.check_phone_number()
user_obj.check_password()


