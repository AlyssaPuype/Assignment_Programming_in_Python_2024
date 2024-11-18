# interaction with database to add, remove, edit, fetch data from the database

from database_manager import DatabaseManager

class StudyTracker:

	def __init__(self, db: DatabaseManager):
		self.db = db


	def add_course(self, arg_list):
		name = arg_list[0]
		added_course = self.db.add_course(name)
		
		if added_course is None:
			return

		print(f"{added_course} added")



"""
	def removeCourse():

	def getCourse():

	def updateCourse():

	def addSession():

	def removeSession():

	def getSession():

	def updateSession():
"""