'''
Single Responsability Principle(S): it's used in order to make a class have only a responsability attached to it.
Problematic Example:
class TaskManager:
    def createTask(self, task):
        return task
    
    def createLog(self, log): # This isn't this class' responsability, therefore a new class must be created for it.
        return log

Solution:
class TaskManager:
    def createTask(self, task):
        return task

class LogManager:
    def createLog(self, log):
        return log
'''

class TaskManager:
    def __init__(self, taskName, taskAge):
        self.taskName = taskName
        self.taskAge = taskAge

    def createTask(self, task):
        return task

class LogManager:
    def __init__(self, logName, logAge):
        self.logName = logName
        self.logAge = logAge

    def createLog(self, log):
        return log
    
Task1 = TaskManager("Jin", 34)
print(Task1.createTask("Study for the exam"))

Log1 = LogManager("Dean", 48)
print(Log1.createLog("That's it for today"))

