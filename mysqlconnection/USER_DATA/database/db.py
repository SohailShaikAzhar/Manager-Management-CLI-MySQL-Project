# import mysql.connector
# import bcrypt

# conn = mysql.connector.connect(
#     database = 'user_data',
#     host = 'localhost',
#     user = 'root',
#     password = 'root'
# )

# cursor = conn.cursor()

# def password_hashing(password):
#     pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
#     return pw

# def create_user(name, email, password):
#     cursor.execute('insert into data1(name, email, password) values(%s,%s,%s)', (name, email, password_hashing(password)))
#     conn.commit()
#     print('data saved')

# create_user('Sohail', 'test2@gmail.com', '1234')


from mysql.connector import connect
from validation.pw_vali import password_validator, pw_check

class DataBasePool:
    conn = connect(
        database = 'user_data',
        host = 'localhost',
        user = 'root',
        password = 'root'
    )
    cur = conn.cursor()

    def create_user(self, name, email, password):
        self.cur.execute('INSERT INTO DATA1(NAME, EMAIL, PASSWORD) VALUES(%s,%s,%s)', (name, email, password_validator(password)))
        self.conn.commit()
        print("Data saved")

    def login(self, email, password):
        self.cur.execute('SELECT EMAIL, PASSWORD FROM DATA1 WHERE EMAIL = %s', (email,))
        data = self.cur.fetchone()
        if pw_check(password, data[-1]):
            print('login')
        else:
            print('Enter correct password')
            pass_count -= 1

    def create_task(self, taskname, taskdesc, userid):
        self.cur.execute('INSERT INTO TASK_TABLE(TASK_NAME, TASK_DESC, USER_ID) VALUES(%s,%s,%s)', (taskname, taskdesc, userid))
        print('Task added successfully')