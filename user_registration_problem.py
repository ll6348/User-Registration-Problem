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
            print("Rule 2 - Should have at least 1 Upper Case")
            print("Rule 3 - Should have at least 1 numeric number in the password")
            print("Rule 4 - Has exactly 1 Special Character")
            self.password = input("Please enter your password: ")
            if re.fullmatch(r'^(?=^[a-zA-Z0-9]*[^a-zA-Z0-9\s_][a-zA-Z0-9]*$)(?=.*[A-Z])(?=.*[0-9]).{8,}$', self.password):
                print("Password passed all rules.")
                is_true = False
            if re.fullmatch(r'^.{1,7}$', self.password):
                 print("Password didn't pass the rule 1.")
                 continue
            if re.fullmatch(r'^(?!.*[A-Z]).{8,}$', self.password):
                 print("Password didn't pass the rule 2.")
                 continue
            if re.fullmatch(r'^(?!.*[0-9]).{8,}$', self.password):
                 print("Password didn't pass the rule 3.")
                 continue
            if not re.fullmatch(r'^[a-zA-Z0-9]*[^a-zA-Z0-9\s_][a-zA-Z0-9]*$', self.password):
                 print("Password didn't pass the rule 4.")
                 continue

class CheckMails(UserRegistrationProblem):
    
    def check_mail(self, email):
        self.email = email
        if re.fullmatch(r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+(\.[a-zA-Z]{2,}){1,2}$', self.email):
            return "Email is accepted"
        else:
            return "Invalid Input."
              
# user_obj = UserRegistrationProblem()
# user_obj.check_first_name()
# user_obj.check_last_name()
# user_obj.check_mail()
# user_obj.check_phone_number()
# user_obj.check_password()
mails_to_check = ['abc@yahoo.com', 'abc-100@yahoo.com', 'abc.100@yahoo.com', 'abc111@abc.com','abc-100@abc.net', 'abc.100@abc.com.au', 'abc@1.com', 'abc@gmail.com.com', 'abc+100@gmail.com']
for i in mails_to_check:
    mail_obj = CheckMails()
    result = mail_obj.check_mail(i)
    print(result)
