# interaction with database to add, remove, edit, fetch data from the database

from database_manager import DatabaseManager

class StudyTracker:

    def __init__(self, db: DatabaseManager):
        self.db = db

# application-related methods:

	# shows a list of commands
    def show_commands(self):
        print("List of commands:")
        print("""
        Courses:
            - 'add course [course_name]'
            - 'remove course [course_id]'
            - 'view course [course_id]'
            - 'update course [course_id]'
        -------------------------------------------------------------
        Sessions:
            - 'add session [course_id, date, subject, status, hours]'        
            - 'remove session [session_id]'
            - 'view session [session_id]'
            - 'update session [column, new content]'
        """)

# course related methods:
    def add_course(self, arg_list):
        name = arg_list[0]
        added_course = self.db.create_course(name)
        
        if added_course is None:
            return

        print(f"{added_course} added")

    

# session related methods:
    """
    def removeCourse():

    def getCourse():

    def updateCourse():

    def addSession():

    def removeSession():

    def getSession():

    def updateSession():
    """
