import bcrypt
import re

def pass_check(password):
    return re.match(r'''^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:";'.,<>/?\\|~-]).{8,}$''', password)

def password_validator(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def pw_check(normal_pw, hash_pw):
    return bcrypt.checkpw(normal_pw.encode('utf-8'),hash_pw.encode('utf-8'))