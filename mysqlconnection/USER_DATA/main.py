from database.db import DataBasePool
from user.usermanager import UserManager
from task.taskmanager import TaskManager

db_obj = DataBasePool()
User_obj = UserManager(db_obj)
Task_obj = TaskManager(db_obj)

while True:
    ch = int(input("Enter \n1 to create user \n2 to login: \n3 to create task\n4 to exit \nChoose one: ").strip())

    match ch:
        case 1:
            name = input("Enter your name: ").strip()
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ").strip()
            User_obj.create_user_obj(name, email, password)
        case 2:
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ").strip()
            User_obj.user_login(email, password)
        case 3:
            taskname = input("Enter task name: ").strip()
            taskdesc = input("Enter task description: ").strip()
            userid = int(input("Enter your user ID: ").strip())
            Task_obj.create_task_obj(taskname, taskdesc, userid)
        case 4:
            break