import re

def email_validator(email):
    return re.match(r'[a-zA-Z0-9_.$#%&*]{5,}\@(gmail|hotmail|yahoo|zoho)\.(com|in|us|uk)', email)