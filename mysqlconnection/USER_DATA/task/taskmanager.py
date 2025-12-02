class TaskManager:
    def __init__(self, db):
        self.db = db

    def create_task_obj(self, taskname, taskdesc, userid):
        self.taskname = taskname
        self.taskdesc = taskdesc
        self.userid = userid
        self.db.create_task(self.taskname, self.taskdesc, self.userid)