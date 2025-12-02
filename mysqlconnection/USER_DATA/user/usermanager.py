from validation.email_vali import email_validator
from validation.pw_vali import pass_check

class UserManager:
    def __init__(self, db):
        self.db = db

    def create_user_obj(self, name, email, password):

        

        if (email_validator(email)) and (pass_check(password)):
            self.name = name
            self.email = email
            self.password = password
            self.db.create_user(self.name, self.email, self.password)
        else:
            try:
                raise TypeError
            except:
                print('enter the email properly or password')
  

    def user_login(self, email, password):
        self.db.login(email, password)